from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    spotify_access_token = models.CharField(max_length=255, null=True, blank=True)
    spotify_refresh_token = models.CharField(max_length=255, null=True, blank=True)
    spotify_token_expires_at = models.DateTimeField(null=True, blank=True)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
class Mood(models.Model):
    name = models.CharField(max_length=100)
    genres = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
    
class MoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class MoodPlaylist(models.Model):
    name = models.CharField(max_length=100)
    spotify_playlist_id = models.CharField(max_length=100)
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE)

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    spotify_id = models.CharField(max_length=100)
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE, null=True, blank=True)
    mood_playlist = models.ForeignKey(MoodPlaylist, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
