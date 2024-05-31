from rest_framework import generics
from .models import User, Mood, MoodEntry, MoodPlaylist, Song
from .serializers.common import UserSerializer, MoodSerializer, MoodEntrySerializer, MoodPlaylistSerializer, SongSerializer
from .serializers.populated import PopulatedUserSerializer, PopulatedMoodSerializer, PopulatedMoodEntrySerializer, PopulatedMoodPlaylistSerializer, PopulatedSongSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from lib.permissions import IsOwnerOrReadOnly
from lib.views import ObjectOwnerView

class UserIndexView(ObjectOwnerView, generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PopulatedUserSerializer
        return UserSerializer

class MoodIndexView(generics.ListCreateAPIView):
    queryset = Mood.objects.all()
    serializer_class = MoodSerializer

class MoodDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mood.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PopulatedMoodSerializer
        return MoodSerializer

class MoodEntryIndexView(ObjectOwnerView, generics.ListCreateAPIView):
    queryset = MoodEntry.objects.all()
    serializer_class = MoodEntrySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class MoodEntryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MoodEntry.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PopulatedMoodEntrySerializer
        return MoodEntrySerializer

class MoodPlaylistIndexView(ObjectOwnerView, generics.ListCreateAPIView):
    queryset = MoodPlaylist.objects.all()
    serializer_class = MoodPlaylistSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class MoodPlaylistDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MoodPlaylist.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PopulatedMoodPlaylistSerializer
        return MoodPlaylistSerializer

class SongIndexView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PopulatedSongSerializer
        return SongSerializer