from django.urls import path

from .api_list.fpl_api.fpl_views import match_day_list, players_list
from .api_list.youtube_api.youtube_views import \
    single_youtube_video, \
    youtube_playlist, \
    single_youtube_playlist, YoutubeApiView

urlpatterns = [
    # FPL API
    path("fpl_matches/", match_day_list, name="fpl_matches"),
    path("fpl_players/", players_list, name="fpl_players"),
    # Youtube API
    # path("youtube_videos/", youtube_videos_list, name="youtube_videos"),
    path("youtube_videos/<str:video_id>/", single_youtube_video, name="single_youtube_video"),
    path("youtube_playlists/", youtube_playlist, name="youtube_playlists"),
    path('youtube_playlists/<str:playlist_id>/', single_youtube_playlist, name="single_youtube_playlist"),
    # Instagram API
    path("youtube_videos/",  YoutubeApiView.as_view(), name="instagram_posts"),
]
