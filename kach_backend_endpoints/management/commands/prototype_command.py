from django.core.management.base import BaseCommand

from kach_api_endpoints.api_list.youtube_api.youtube_model import YoutubeVideo, YoutubePlaylist


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("prototype command")

        playlist_videos = YoutubePlaylist.objects.filter(playlist_name="ufc_fights")

        print(playlist_videos)