from django.db.models import Q, Count
from rest_framework import generics, status
from django.db import IntegrityError
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
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from .spotify_utils import get_spotify_client, SpotifyOAuth
from .credentials import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)

@login_required
def connect_spotify(request):
    user = request.user
    if not user.spotify_access_token:
        # User is not connected to Spotify, redirect to the Spotify authorization URL
        auth_manager = SpotifyOAuth(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            scope='user-library-read playlist-modify-private playlist-read-private',
        )
        authorization_url = auth_manager.get_authorize_url()
        return JsonResponse({'redirect_url': authorization_url})

    # User is already connected to Spotify, redirect to the mood-entry page
    return JsonResponse({'redirect_url': None})

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

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = UserSerializer(request.user)
        return Response(user.data)
    
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
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET': 
            return PopulatedMoodPlaylistSerializer
        else:
            return MoodPlaylistSerializer

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
    permission_classes = [AllowAny] 

class LoginView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer
    
# def get_recommended_songs(mood, user):
#     # Get songs associated with the selected mood
#     mood_songs = Song.objects.filter(mood=mood)

#     # Get songs associated with playlists of the selected mood that are owned by the user
#     mood_playlists = MoodPlaylist.objects.filter(mood=mood, owner=user)
#     playlist_songs = Song.objects.filter(mood_playlist__in=mood_playlists)

#     # Combine the songs from the mood and playlists, removing duplicates
#     recommended_songs = (mood_songs | playlist_songs).distinct()

#     # Filter songs based on the genres associated with the mood (if any)
#     if mood.genres:
#         genre_list = mood.genres.split(',')
#         recommended_songs = recommended_songs.filter(
#             Q(artist__icontains=genre_list[0]) |
#             Q(title__icontains=genre_list[0]) |
#             Q(artist__icontains=genre_list[1]) |
#             Q(title__icontains=genre_list[1])
#         )

#     return recommended_songs


# class MoodPlaylistCreateView(generics.CreateAPIView):
#     queryset = MoodPlaylist.objects.all()
#     serializer_class = MoodPlaylistSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         try:
#             mood = Mood.objects.get(id=self.request.data['mood'])
#             serializer.save(owner=self.request.user, mood=mood)
#         except Mood.DoesNotExist:
#             raise serializers.ValidationError('Mood does not exist')
#         except IntegrityError:
#             raise serializers.ValidationError('Duplicate playlist name for the user and mood')

def get_personalized_recommendations(user, limit=10):
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

# 

#this is the view w/o spotify
def get_recommended_songs(mood, user):
    # Get songs associated with the selected mood
    mood_songs = Song.objects.filter(mood=mood)

    # Get songs associated with playlists of the selected mood that are owned by the user
  
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

class MoodRecommendationsView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, mood_id):
        try:
            # mood = Mood.objects.get(id=mood_id)
            # recommended_songs = get_recommended_songs(mood, request.user)
            songs = Song.objects.filter(mood=mood_id)
            serializer = SongSerializer(songs, many=True)
            return Response(serializer.data)
        except Mood.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class MoodPlaylistCreateView(generics.CreateAPIView):
    queryset = MoodPlaylist.objects.all()
    serializer_class = MoodPlaylistSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        mood_id = self.request.data.get('mood')
        if mood_id:
            try:
                mood = Mood.objects.get(id=mood_id)
                playlist_name = mood.name
                serializer.save(owner=self.request.user, mood=mood, name=playlist_name)
            except Mood.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': 'Missing mood field'})
# class AssociateSongsWithPlaylistView(APIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         playlist_id = request.data.get('playlist_id')
#         if playlist_id:
#             try:
#                 playlist = MoodPlaylist.objects.get(id=playlist_id)
#                 mood = playlist.mood
#                 songs = Song.objects.filter(mood=mood)

#                 for song in songs:
#                     song.mood_playlist = playlist
#                     song.save()

#                 return Response(status=status.HTTP_200_OK)
#             except MoodPlaylist.DoesNotExist:
#                 return Response(status=status.HTTP_404_NOT_FOUND)
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': 'Missing playlist_id field'})

class AssociateSongsWithPlaylistView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        song = request.data.get('song')
        # print(song)
        song_to_update = Song.objects.get(pk=song.get('id'))
        if song:
            try:
                print(song.get('mood'))
                playlist_to_find = MoodPlaylist.objects.get(mood=song.get('mood'))
                playlist = MoodPlaylistSerializer(playlist_to_find)
                print('plalist already exists')
            except MoodPlaylist.DoesNotExist:
                populated_song= PopulatedSongSerializer(song_to_update)
                print(populated_song.data)

                new_playlist= {
                  'name' : populated_song.data.get('mood').get('name'),
                  'mood' : song.get('mood'),
                  'owner' : request.user.id
                }
                playlist = MoodPlaylistSerializer(data=new_playlist)
                if playlist.is_valid():
                    playlist.save()

                    print('playlist created')
            
            serialized_song = SongSerializer(song_to_update)

            if playlist not in song_to_update.mood_playlist.all():
                print('adding to playlist')
                song_to_update.mood_playlist.add(playlist.data.get('id'))
                song_to_update.save()
            else:
                print('already in playlist')
            return Response(status=status.HTTP_201_CREATED)
        
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': 'Missing playlist_id field'})
                          
class UserRecommendationsView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        recommended_songs = get_personalized_recommendations(user, limit=10)
        serializer = SongSerializer(recommended_songs, many=True)
        return Response(serializer.data)