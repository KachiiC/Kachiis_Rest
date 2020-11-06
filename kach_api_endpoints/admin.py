from django.contrib import admin
from kach_api_endpoints.youtube_api.youtube_model import YoutubeVideo, YoutubePlaylist

admin.site.register(YoutubeVideo)
admin.site.register(YoutubePlaylist)