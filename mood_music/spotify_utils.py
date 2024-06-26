import spotipy
from spotipy.oauth2 import SpotifyOAuth
from .models import User, Mood, MoodPlaylist, Song
from .credentials import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

def get_spotify_client(user):
    auth_manager = SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope='user-library-read playlist-modify-private playlist-read-private',
    )
    auth_manager.get_access_token(user.spotify_refresh_token)
    return spotipy.Spotify(auth_manager=auth_manager)

def fetch_mood_playlists(mood):
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

def fetch_playlist_songs(mood_playlist):
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