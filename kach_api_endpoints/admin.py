from django.contrib import admin
from kach_api_endpoints.api_list.youtube_api.youtube_model import YoutubeVideo, YoutubePlaylist
from kach_api_endpoints.api_list.music_chart_api.music_chart_model import Song
from kach_api_endpoints.api_list.fpl_api.fpl_model import Player, MatchDay
from kach_api_endpoints.api_list.imdb_api.imdb_model import Content

admin.site.register(Content)  # IMDB API
admin.site.register(Player)  # FPL API
admin.site.register(MatchDay)  # FPL API
admin.site.register(Song)  # Music API
admin.site.register(YoutubeVideo)  # Youtube API
admin.site.register(YoutubePlaylist)  # Youtube API