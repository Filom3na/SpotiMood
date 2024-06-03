from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    spotify_access_token = models.CharField(max_length=255, null=True, blank=True)
    spotify_refresh_token = models.CharField(max_length=255, null=True, blank=True)
    spotify_token_expires_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.username
class Mood(models.Model):
    name = models.CharField(max_length=100)
    genres = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='moods')

    def __str__(self):
        return self.name

class MoodEntry(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mood_entries')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='mood_entries',  default=1)
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_mood_entries')

    def __str__(self):
        return f"{self.user.username}'s {self.mood.name} entry"

class MoodPlaylist(models.Model):
    name = models.CharField(max_length=100)
    spotify_playlist_id = models.CharField(max_length=100)
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE, related_name='playlists')
    # owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_mood_playlists')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owned_mood_playlists',  default=1)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    spotify_id = models.CharField(max_length=100)
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE, null=True, blank=True, related_name='songs')
    mood_playlist = models.ForeignKey(MoodPlaylist, on_delete=models.CASCADE, null=True, blank=True, related_name='songs')

    def __str__(self):
        return f"{self.title} by {self.artist}"
