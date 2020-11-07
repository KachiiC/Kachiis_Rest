from django.urls import path
from kach_api_endpoints.api_list.fpl_api import fpl_views
from kach_api_endpoints.api_list.music_chart_api import music_chart_view
from kach_api_endpoints.api_list.youtube_api import youtube_views

urlpatterns = [
    # FPL API
    path("fpl_players/", fpl_views.players_list, name="fpl_players"),
    # Music Chart API
    path("music_charts/", music_chart_view.chart_list, name="music_chart"),
    path("music_charts/<int:chart_number>/", music_chart_view.chart_position, name="chart_position"),
    # Youtube API
    path("youtube_videos/", youtube_views.youtube_videos_list, name="youtube_videos"),
    path("youtube_videos/<str:video_id>/", youtube_views.single_youtube_video, name="single_youtube_video"),
    path("youtube_playlists/", youtube_views.youtube_playlist, name="youtube_playlists"),
    path('youtube_playlists/<str:playlist_id>/', youtube_views.single_youtube_playlist, name="single_youtube_playlist")
]
