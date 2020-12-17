from django.urls import path
from .api_list.fpl_api.fpl_views import match_day_list, players_list
from .api_list.music_chart_api.music_chart_view import chart_list, chart_position
from .api_list.youtube_api.youtube_views import \
    single_youtube_video, \
    youtube_videos_list, \
    youtube_playlist, \
    single_youtube_playlist

urlpatterns = [
    # FPL API
    path("fpl_matches/", match_day_list, name="fpl_matches"),
    path("fpl_players/", players_list, name="fpl_players"),
    # Music Chart API
    path("music_charts/", chart_list, name="music_chart"),
    path("music_charts/<int:chart_number>/", chart_position, name="chart_position"),
    # Youtube API
    path("youtube_videos/", youtube_videos_list, name="youtube_videos"),
    path("youtube_videos/<str:video_id>/", single_youtube_video, name="single_youtube_video"),
    path("youtube_playlists/", youtube_playlist, name="youtube_playlists"),
    path('youtube_playlists/<str:playlist_id>/', single_youtube_playlist, name="single_youtube_playlist")
]
