from django.contrib import admin
from .api_list.youtube_api.youtube_model import YoutubeVideo, YoutubePlaylist
from .api_list.fpl_api.fpl_model import Player, MatchDay

admin.site.register(Player)  # FPL API
admin.site.register(MatchDay)  # FPL API
admin.site.register(YoutubeVideo)  # Youtube API
admin.site.register(YoutubePlaylist)  # Youtube API
