from django.urls import path
from kach_api_endpoints.youtube_api import youtube_views

urlpatterns = [
    path("youtube_videos/", youtube_views.youtube_videos_list, name="youtube_videos"),
    path("youtube_videos/<str:video_id>/", youtube_views.single_youtube_video, name="single_youtube_video"),
    path("youtube_playlists/", youtube_views.youtube_playlist, name="youtube_playlists"),
    path('youtube_playlists/<str:playlist_id>/', youtube_views.single_youtube_playlist, name="single_youtube_playlist")
]
