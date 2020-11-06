from django.core.management.base import BaseCommand
import os
# Models
from kach_api_endpoints.youtube_api.youtube_model import YoutubeVideo, YoutubePlaylist
from kach_api_endpoints.management.repoppers.youtube_video import create_new_youtube_videos

YOUTUBE_DATA_DIR = os.getcwd() + "/kach_api_endpoints/data/youtube/"

# place your data here
repop_data = ["fightHighlightsData.json", "ufcFightsData.json"]

new_playlists = [
    {
        "playlist_name": "UFC Fights",
        "playlist_id": "PLaaEeFtNlIJ1QCSWkBvxItbKYEpGENASC"
    },
    {
        "playlist_name": "Fight Highlights",
        "playlist_id": "PLaaEeFtNlIJ2Yigy4wHCQlcuRZg4NKbi5"
    }
]


class Command(BaseCommand):

    def handle(self, *args, **options):
        """" Deletes all Videos/Playlists and repopulates them the the prep_youtube data"""
        YoutubeVideo.objects.all().delete()
        YoutubePlaylist.objects.all().delete()

        for file in repop_data:
            create_new_youtube_videos(YOUTUBE_DATA_DIR + file)
            print(f"successfully added {file}")

        for playlist in new_playlists:
            YoutubePlaylist(
                playlist_name=playlist["playlist_name"],
                playlist_id=playlist["playlist_id"]
            ).save()
            print(f"successfully created {playlist['playlist_name']}")

        all_videos = YoutubeVideo.objects.all()
        all_playlists = YoutubePlaylist.objects.all()

        for video in all_videos:
            for playlist in all_playlists:
                if video.playlist_id == playlist.playlist_id:
                    correct_playlist = YoutubePlaylist.objects.get(playlist_id=video.playlist_id)
                    correct_playlist.playlist_videos.add(video)

        print("successfully added to all videos to playlists")
        print("Repop complete!")
