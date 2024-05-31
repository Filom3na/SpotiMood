from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import User, Mood, MoodEntry, MoodPlaylist, Song
from .serializers.common import UserSerializer, MoodSerializer, MoodEntrySerializer, MoodPlaylistSerializer, SongSerializer
from .serializers.populated import PopulatedUserSerializer, PopulatedMoodSerializer, PopulatedMoodEntrySerializer, PopulatedMoodPlaylistSerializer, PopulatedSongSerializer

class UserListCreateAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = PopulatedUserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MoodListCreateAPIView(APIView):
    def get(self, request):
        moods = Mood.objects.all()
        serializer = MoodSerializer(moods, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MoodDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Mood.objects.get(pk=pk)
        except Mood.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        mood = self.get_object(pk)
        serializer = PopulatedMoodSerializer(mood)
        return Response(serializer.data)
    
    def put(self, request, pk):
        mood = self.get_object(pk)
        serializer = MoodSerializer(mood, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        mood = self.get_object(pk)
        mood.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MoodEntryListCreateAPIView(APIView):
    def get(self, request):
        mood_entries = MoodEntry.objects.all()
        serializer = MoodEntrySerializer(mood_entries, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MoodEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MoodEntryDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return MoodEntry.objects.get(pk=pk)
        except MoodEntry.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        mood_entry = self.get_object(pk)
        serializer = PopulatedMoodEntrySerializer(mood_entry)
        return Response(serializer.data)
    
    def put(self, request, pk):
        mood_entry = self.get_object(pk)
        serializer = MoodEntrySerializer(mood_entry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        mood_entry = self.get_object(pk)
        mood_entry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MoodPlaylistListCreateAPIView(APIView):
    def get(self, request):
        mood_playlists = MoodPlaylist.objects.all()
        serializer = MoodPlaylistSerializer(mood_playlists, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MoodPlaylistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MoodPlaylistDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return MoodPlaylist.objects.get(pk=pk)
        except MoodPlaylist.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        mood_playlist = self.get_object(pk)
        serializer = PopulatedMoodPlaylistSerializer(mood_playlist)
        return Response(serializer.data)
    
    def put(self, request, pk):
        mood_playlist = self.get_object(pk)
        serializer = MoodPlaylistSerializer(mood_playlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        mood_playlist = self.get_object(pk)
        mood_playlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SongListCreateAPIView(APIView):
    def get(self, request):
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SongDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Song.objects.get(pk=pk)
        except Song.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        song = self.get_object(pk)
        serializer = PopulatedSongSerializer(song)
        return Response(serializer.data)
    
    def put(self, request, pk):
        song = self.get_object(pk)
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        song = self.get_object(pk)
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)