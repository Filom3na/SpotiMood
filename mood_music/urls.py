from django.urls import path
from .views import (
    UserIndexView, UserDetailView,
    MoodIndexView, MoodDetailView,
    MoodEntryIndexView, MoodEntryDetailView,
    MoodPlaylistIndexView, MoodPlaylistDetailView,
    SongIndexView, SongDetailView
)
from .views_apiview import (
    UserListCreateAPIView, UserDetailAPIView,
    MoodListCreateAPIView, MoodDetailAPIView,
    MoodEntryListCreateAPIView, MoodEntryDetailAPIView,
    MoodPlaylistListCreateAPIView, MoodPlaylistDetailAPIView,
    SongListCreateAPIView, SongDetailAPIView
)

urlpatterns = [
    # URLs for generic views
    path('users/', UserIndexView.as_view(), name='user-index'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('moods/', MoodIndexView.as_view(), name='mood-index'),
    path('moods/<int:pk>/', MoodDetailView.as_view(), name='mood-detail'),
    path('mood-entries/', MoodEntryIndexView.as_view(), name='mood-entry-index'),
    path('mood-entries/<int:pk>/', MoodEntryDetailView.as_view(), name='mood-entry-detail'),
    path('mood-playlists/', MoodPlaylistIndexView.as_view(), name='mood-playlist-index'),
    path('mood-playlists/<int:pk>/', MoodPlaylistDetailView.as_view(), name='mood-playlist-detail'),
    path('songs/', SongIndexView.as_view(), name='song-index'),
    path('songs/<int:pk>/', SongDetailView.as_view(), name='song-detail'),
    
    # URLs for APIView-based views
    path('api/users/', UserListCreateAPIView.as_view(), name='user-list-api'),
    path('api/users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail-api'),
    path('api/moods/', MoodListCreateAPIView.as_view(), name='mood-list-api'),
    path('api/moods/<int:pk>/', MoodDetailAPIView.as_view(), name='mood-detail-api'),
    path('api/mood-entries/', MoodEntryListCreateAPIView.as_view(), name='mood-entry-list-api'),
    path('api/mood-entries/<int:pk>/', MoodEntryDetailAPIView.as_view(), name='mood-entry-detail-api'),
    path('api/mood-playlists/', MoodPlaylistListCreateAPIView.as_view(), name='mood-playlist-list-api'),
    path('api/mood-playlists/<int:pk>/', MoodPlaylistDetailAPIView.as_view(), name='mood-playlist-detail-api'),
    path('api/songs/', SongListCreateAPIView.as_view(), name='song-list-api'),
    path('api/songs/<int:pk>/', SongDetailAPIView.as_view(), name='song-detail-api'),
]