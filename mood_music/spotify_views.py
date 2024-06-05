import spotipy
from spotipy.oauth2 import SpotifyOAuth
from django.shortcuts import redirect
from .credentials import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
from .models import User, Mood, MoodPlaylist, Song
from django.contrib.auth.decorators import login_required
import logging

logger = logging.getLogger(__name__)

@login_required
def spotify_authorize(request):
    scope = 'user-library-read playlist-modify-private playlist-read-private'
    auth_manager = SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=scope,
    )
    authorization_url = auth_manager.get_authorize_url()
    return redirect(authorization_url)

@login_required
def spotify_callback(request):
    try:
        auth_manager = SpotifyOAuth(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            scope='user-library-read playlist-modify-private playlist-read-private',
        )
        code = request.GET.get('code')
        token_info = auth_manager.get_access_token(code)

        user = request.user
        user.spotify_access_token = token_info['access_token']
        user.spotify_refresh_token = token_info['refresh_token']
        user.spotify_token_expires_at = token_info['expires_at']
        user.save()

        return redirect('client/src/components/pages/SongRecommendation.jsx')  

    except Exception as e:
        logger.error(f"Error during Spotify callback: {str(e)}")
        return redirect('error')  # Redirect to an error page

def get_spotify_client(user):
    try:
        auth_manager = SpotifyOAuth(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            scope='user-library-read playlist-modify-private playlist-read-private',
        )
        auth_manager.refresh_access_token(user.spotify_refresh_token)
        return spotipy.Spotify(auth_manager=auth_manager)
    except Exception as e:
        logger.error(f"Error getting Spotify client for user {user.id}: {str(e)}")
        raise

def fetch_mood_playlists(mood):
    try:
        user = mood.user
        spotify = get_spotify_client(user)
        playlists = spotify.category_playlists(category_id=mood.name.lower())
        for playlist in playlists['playlists']['items']:
            mood_playlist, created = MoodPlaylist.objects.get_or_create(
                spotify_playlist_id=playlist['id'],
                mood=mood,
                defaults={'name': playlist['name']}
            )
            if created:
                fetch_playlist_songs(mood_playlist)
    except Exception as e:
        logger.error(f"Error fetching mood playlists for mood {mood.id}: {str(e)}")
        raise

def fetch_playlist_songs(mood_playlist):
    try:
        user = mood_playlist.mood.user
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