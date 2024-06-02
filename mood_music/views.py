from django.db.models import Q, Count
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User, Mood, MoodEntry, MoodPlaylist, Song
from .serializers.common import UserSerializer, MoodSerializer, MoodEntrySerializer, MoodPlaylistSerializer, SongSerializer
from .serializers.populated import PopulatedUserSerializer, PopulatedMoodSerializer, PopulatedMoodEntrySerializer, PopulatedMoodPlaylistSerializer, PopulatedSongSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


@login_required
def connect_spotify(request):
    user = request.user
    if not user.spotify_access_token:
        # User is not connected to Spotify, redirect to the Spotify authorization URL
        return redirect(reverse('spotify-authorize'))

    # User is already connected to Spotify, redirect to the profile or desired page
    return redirect('profile')

class UserIndexView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()

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

class MoodEntryIndexView(generics.ListCreateAPIView):
    queryset = MoodEntry.objects.all()
    serializer_class = MoodEntrySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, owner=self.request.user)

class MoodEntryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MoodEntry.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PopulatedMoodEntrySerializer
        return MoodEntrySerializer

class MoodPlaylistIndexView(generics.ListCreateAPIView):
    queryset = MoodPlaylist.objects.all()
    serializer_class = MoodPlaylistSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class MoodPlaylistDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MoodPlaylist.objects.all()

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

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer
    
def get_recommended_songs(mood, user):
    """
    Retrieve recommended songs based on the user's selected mood, using a combination of mood-genre mapping and mood-based playlists.
    """
    # Get songs associated with the selected mood
    mood_songs = Song.objects.filter(mood=mood)

    # Get songs associated with playlists of the selected mood that are owned by the user
    mood_playlists = MoodPlaylist.objects.filter(mood=mood, owner=user)
    playlist_songs = Song.objects.filter(mood_playlist__in=mood_playlists)

    # Combine the songs from the mood and playlists, removing duplicates
    recommended_songs = (mood_songs | playlist_songs).distinct()

    # Filter songs based on the genres associated with the mood (if any)
    if mood.genres:
        genre_list = mood.genres.split(',')
        recommended_songs = recommended_songs.filter(
            Q(artist__icontains=genre_list[0]) |
            Q(title__icontains=genre_list[0]) |
            Q(artist__icontains=genre_list[1]) |
            Q(title__icontains=genre_list[1])
        )

    return recommended_songs

def get_personalized_recommendations(user, limit=10):
    """
    Retrieve personalized song recommendations based on the user's mood history.
    """
    # Get the user's most frequent moods
    user_moods = user.moods.annotate(mood_count=Count('moodentry')).order_by('-mood_count')[:3]

    # Get songs associated with the user's most frequent moods
    mood_songs = Song.objects.filter(mood__in=user_moods)

    # Get songs associated with playlists of the user's most frequent moods
    mood_playlists = MoodPlaylist.objects.filter(mood__in=user_moods, owner=user)
    playlist_songs = Song.objects.filter(mood_playlist__in=mood_playlists)

    # Combine the songs from the moods and playlists, removing duplicates
    recommended_songs = (mood_songs | playlist_songs).distinct()

    # Filter songs based on the genres associated with the user's most frequent moods
    genre_list = [mood.genres for mood in user_moods if mood.genres]
    if genre_list:
        recommended_songs = recommended_songs.filter(
            Q(artist__icontains=genre_list[0]) |
            Q(title__icontains=genre_list[0]) |
            Q(artist__icontains=genre_list[1]) |
            Q(title__icontains=genre_list[1])
        )

    return recommended_songs[:limit]

class MoodRecommendationsView(APIView):
    def get(self, request, mood_id):
        mood = Mood.objects.get(id=mood_id)
        recommended_songs = get_recommended_songs(mood, request.user)
        serializer = SongSerializer(recommended_songs, many=True)
        return Response(serializer.data)

class UserRecommendationsView(APIView):
    def get(self, request):
        user = request.user
        recommended_songs = get_personalized_recommendations(user, limit=10)
        serializer = SongSerializer(recommended_songs, many=True)
        return Response(serializer.data)