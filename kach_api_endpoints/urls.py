from django.urls import path

from .api_list.fpl_api.fpl_views import match_day_list, players_list
from .api_list.youtube_api.youtube_views import \
    single_youtube_video, \
    youtube_playlist, \
    youtube_videos_list, \
    single_youtube_playlist, YoutubeApiView
from .api_list.instagram_api.instagram_views import instagram_posts_list, InstagramPostApiView

urlpatterns = [
    # FPL API
    path("fpl_matches/", match_day_list, name="fpl_matches"),
    path("fpl_players/", players_list, name="fpl_players"),
    # Youtube API
    path("youtube_videos/", youtube_videos_list, name="youtube_videos"),
    path("youtube_videos_refresh/", YoutubeApiView.as_view(), name="youtube_videos_refresh"),
    path("youtube_videos/<str:video_id>/", single_youtube_video, name="single_youtube_video"),
    path("youtube_playlists/", youtube_playlist, name="youtube_playlists"),
    path('youtube_playlists/<str:playlist_id>/', single_youtube_playlist, name="single_youtube_playlist"),
    # Instagram API
    path("instagram_list_refresh/", InstagramPostApiView.as_view(), name="instagram_posts_refresh"),
    path("instagram_list/", instagram_posts_list, name="instagram_posts")
]
