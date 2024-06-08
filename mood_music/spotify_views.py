import spotipy
from spotipy.oauth2 import SpotifyOAuth
from django.shortcuts import redirect
from django.urls import reverse
from .credentials import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
import datetime
from .models import User, Mood, MoodPlaylist, Song
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import secrets
import logging

logger = logging.getLogger(__name__)

def spotify_authorize(request):
    # Generate a random state string
    state = secrets.token_hex(16)
    request.session['spotify_auth_state'] = state

    # Build the authorization URL
    scope = 'user-read-private user-read-email'
    auth_url = 'https://accounts.spotify.com/authorize'
    auth_url += '?response_type=code'
    auth_url += '&client_id=' + CLIENT_ID
    auth_url += '&scope=' + scope
    auth_url += '&redirect_uri=' + REDIRECT_URI
    auth_url += '&state=' + state

    return redirect(auth_url)

# @csrf_exempt
# def spotify_callback(request):
#     if request.method == 'GET':
#         access_token = request.GET.get('access_token')
#         state = request.GET.get('state')
#         # # Verify the state parameter to prevent CSRF attacks
#         # if state != request.session.get('spotify_auth_state'):
#         #     return JsonResponse({'success': False, 'error': 'Invalid state parameter'}, status=400)
        
#         # Store the access token in the user's session or database
#         user = request.user
#         user.spotify_access_token = access_token
#         user.spotify_refresh_token = request.GET.get('refresh_token', None)
#         user.save()
#         # request.session['spotify_access_token'] = access_token

#         # Redirect the user to the next page or perform any other necessary actions
#         return redirect('http://localhost:5173/mood-entry')
#         # return JsonResponse({'success': True})
#     else:
#         return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=400)


@csrf_exempt
def spotify_callback(request):
    if request.method == 'GET':
        code = request.GET.get('code')
        state = request.GET.get('state')

        # # Verify the state parameter to prevent CSRF attacks
        # if state != request.session.get('spotify_auth_state'):
        #     return JsonResponse({'success': False, 'error': 'Invalid state parameter'}, status=400)

        # Initialize Spotify OAuth to exchange the authorization code for tokens
        sp_oauth = SpotifyOAuth(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            scope='user-read-private user-read-email'
        )
        token_info = sp_oauth.get_access_token(code)
        access_token = token_info.get('access_token')
        refresh_token = token_info.get('refresh_token')

        if not access_token or not refresh_token:
            return JsonResponse({'success': False, 'error': 'Failed to retrieve tokens'}, status=400)

        # Store the access token and refresh token in the user's database record
        user = request.user
        user.spotify_access_token = access_token
        user.spotify_refresh_token = refresh_token
        user.spotify_token_expires_at = datetime.datetime.fromtimestamp(token_info.get('expires_at'))
        user.save()

        # Redirect the user to the next page or perform any other necessary actions
        return redirect('http://localhost:5173/mood-entry')
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=400)


@login_required
def check_spotify_login(request):
    access_token = request.session.get('spotify_access_token')
    if access_token:
        try:
            # Create a Spotify client using the stored access_token
            sp = spotipy.Spotify(auth=access_token)

            # Make a request to the Spotify API to retrieve the current user's profile information
            user_profile = sp.current_user()

            # If the request is successful, return the user's profile information
            return JsonResponse({
                'is_logged_in': True,
                'user_profile': user_profile
            })
        except spotipy.SpotifyException as e:
            # If the request fails, it means the access_token is invalid or has expired
            return JsonResponse({
                'is_logged_in': False,
                'error': str(e)
            })
    else:
        # If there's no access_token stored in the session, the user is not logged in
        return JsonResponse({'is_logged_in': False})
    


def get_spotify_client(user):
    auth_manager = SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope='user-library-read playlist-modify-private playlist-read-private',
        cache_handler=None
    )
    auth_manager.cache_handler.token_info = {
        'access_token': user.spotify_access_token,
        'expires_at': int(user.spotify_token_expires_at.timestamp()),
        'refresh_token': user.spotify_refresh_token
    }
    spotify_client = spotipy.Spotify(auth_manager=auth_manager)
    return spotify_client

# def get_spotify_client(user):
#     try:
#         auth_manager = SpotifyOAuth(
#             client_id=CLIENT_ID,
#             client_secret=CLIENT_SECRET,
#             redirect_uri=REDIRECT_URI,
#             scope='user-library-read playlist-modify-private playlist-read-private',
#             cache_handler=None
#         )
#         auth_manager.cache_handler.token_info = {
#             'access_token': user.spotify_access_token,
#             'expires_at': 0,  # Set expires_at to 0 to force token refresh
#             'refresh_token': None
#         }
#         spotify_client = spotipy.Spotify(auth_manager=auth_manager)
#         return spotify_client
#     except Exception as e:
#         logger.error(f"Error getting Spotify client for user {user.id}: {str(e)}")
#         raise

def fetch_mood_playlists(mood, user):
    try:
        spotify = get_spotify_client(user)
        playlists = spotify.category_playlists(category_id=mood.name.lower())
        for playlist in playlists['playlists']['items']:
            mood_playlist, created = MoodPlaylist.objects.get_or_create(
                spotify_playlist_id=playlist['id'],
                mood=mood,
                defaults={'name': playlist['name']}
            )
            if created:
                fetch_playlist_songs(mood_playlist, user)
    except Exception as e:
        logger.error(f"Error fetching mood playlists for mood {mood.id}: {str(e)}")
        raise

def fetch_playlist_songs(mood_playlist, user):
    try:
        spotify = get_spotify_client(user)
        playlist_tracks = spotify.playlist_items(mood_playlist.spotify_playlist_id)
        for track in playlist_tracks['items']:
            song, created = Song.objects.get_or_create(
                spotify_id=track['track']['id'],
                defaults={
                    'title': track['track']['name'],
                    'artist': ', '.join([artist['name'] for artist in track['track']['artists']]),
                    'mood': mood_playlist.mood,
                    'mood_playlist': mood_playlist,
                }
            )
    except Exception as e:
        logger.error(f"Error fetching songs for mood playlist {mood_playlist.id}: {str(e)}")
        raise