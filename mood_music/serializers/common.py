from rest_framework import serializers
from ..models import User, Mood, MoodEntry, MoodPlaylist, Song

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class MoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = '__all__'

class MoodEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodEntry
        fields = '__all__'

class MoodPlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodPlaylist
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'