from django.contrib import admin
from .models import User, Mood, MoodEntry, MoodPlaylist, Song
# Register your models here.
admin.site.register(User)
admin.site.register(Mood)
admin.site.register(MoodEntry)
admin.site.register(MoodPlaylist)
admin.site.register(Song)