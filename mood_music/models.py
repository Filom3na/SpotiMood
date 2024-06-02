from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    spotify_access_token = models.CharField(max_length=255, null=True, blank=True)
    spotify_refresh_token = models.CharField(max_length=255, null=True, blank=True)
    spotify_token_expires_at = models.DateTimeField(null=True, blank=True)

class Mood(models.Model):
    name = models.CharField(max_length=100)
    genres = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='moods')

class MoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mood_entries')
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_mood_entries')

class MoodPlaylist(models.Model):
    name = models.CharField(max_length=100)
    spotify_playlist_id = models.CharField(max_length=100)
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE, related_name='playlists')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_mood_playlists')

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    spotify_id = models.CharField(max_length=100)
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE, null=True, blank=True, related_name='songs')
    mood_playlist = models.ForeignKey(MoodPlaylist, on_delete=models.CASCADE, null=True, blank=True, related_name='songs')