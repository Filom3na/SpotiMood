from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Mood, MoodEntry, MoodPlaylist, Song
# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Mood)
admin.site.register(MoodEntry)
admin.site.register(MoodPlaylist)
admin.site.register(Song)