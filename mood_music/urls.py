from django.urls import path
from .views import (
    UserIndexView, UserDetailView,
    MoodIndexView, MoodDetailView,
    MoodEntryIndexView, MoodEntryDetailView,
    MoodPlaylistIndexView, MoodPlaylistDetailView,
    SongIndexView, SongDetailView, RegisterView,
    LoginView, MoodRecommendationsView, UserRecommendationsView,
    connect_spotify
)
from .spotify_views import spotify_authorize, spotify_callback

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

    # URLs for user authentication and registration
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),

    # URLs for Spotify integration
    path('spotify-authorize/', spotify_authorize, name='spotify-authorize'),
    path('spotify-callback/', spotify_callback, name='spotify-callback'),

    # URL for connect_spotify view
    path('connect-spotify/', connect_spotify, name='connect-spotify'),

    # URLs for mood and user recommendations
    path('mood-recommendations/<int:mood_id>/', MoodRecommendationsView.as_view(), name='mood-recommendations'),
    path('user-recommendations/', UserRecommendationsView.as_view(), name='user-recommendations'),
]