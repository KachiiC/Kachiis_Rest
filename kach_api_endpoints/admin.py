from django.contrib import admin
from kach_api_endpoints.api_list.youtube_api.youtube_model import YoutubeVideo, YoutubePlaylist
from kach_api_endpoints.api_list.music_chart_api.music_chart_model import Song

# Music API
admin.site.register(Song)
# Youtube API
admin.site.register(YoutubeVideo)
admin.site.register(YoutubePlaylist)