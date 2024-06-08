from .common import UserSerializer, MoodSerializer, MoodEntrySerializer, MoodPlaylistSerializer, SongSerializer

class PopulatedUserSerializer(UserSerializer):
    mood_entries = MoodEntrySerializer(many=True, read_only=True)
    playlists = MoodPlaylistSerializer(many=True, read_only=True)

class PopulatedMoodSerializer(MoodSerializer):
    mood_entries = MoodEntrySerializer(many=True, read_only=True)
    playlists = MoodPlaylistSerializer(many=True, read_only=True)
    songs = SongSerializer(many=True, read_only=True)

class PopulatedMoodEntrySerializer(MoodEntrySerializer):
    user = UserSerializer(read_only=True)
    mood = MoodSerializer(read_only=True)

class PopulatedMoodPlaylistSerializer(MoodPlaylistSerializer):
    mood = MoodSerializer(read_only=True)
    songs = SongSerializer(many=True, read_only=True)

class PopulatedSongSerializer(SongSerializer):
    mood = MoodSerializer(read_only=True)
    mood_playlist = MoodPlaylistSerializer(many=True, read_only=True)