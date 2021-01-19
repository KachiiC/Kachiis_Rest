from django.contrib import admin
from .api_list.youtube_api.youtube_model import YoutubeVideo, YoutubePlaylist
from .api_list.fpl_api.fpl_model import Player, MatchDay
from .api_list.instagram_api.instagram_model import Post

admin.site.register(Player)  # FPL API
admin.site.register(MatchDay)  # FPL API
admin.site.register(YoutubeVideo)  # Youtube API
admin.site.register(YoutubePlaylist)  # Youtube API
admin.site.register(Post)
