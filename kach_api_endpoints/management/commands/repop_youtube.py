from django.core.management.base import BaseCommand
import os
import json
# Models
from kach_api_endpoints.api_list.youtube_api.youtube_model import YoutubeVideo, YoutubePlaylist
from kach_api_endpoints.management.repoppers.youtube_video_repoppers import create_new_youtube_videos


YOUTUBE_DATA_DIR = os.getcwd() + "/kach_api_endpoints/data/youtube/"


class Command(BaseCommand):

    def handle(self, *args, **options):
        """" Deletes all Videos/Playlists and repopulates them the the prep_youtube data"""
        YoutubeVideo.objects.all().delete()
        YoutubePlaylist.objects.all().delete()

        with open(f"{YOUTUBE_DATA_DIR}playlistData.json", 'r') as json_file:
            repop_data = json.load(json_file)

        for file in repop_data:
            create_new_youtube_videos(YOUTUBE_DATA_DIR + f"playlists/{file['playlist_name']}.json")
            print(f"Successfully added videos from {file['playlist_name']}.json")

        for playlist in repop_data:
            YoutubePlaylist(
                playlist_name=playlist["playlist_name"],
                playlist_id=playlist["playlist_id"]
            ).save()
            print(f"Successfully created {playlist['playlist_name']} playlist")

        all_videos = YoutubeVideo.objects.all()
        all_playlists = YoutubePlaylist.objects.all()

        for video in all_videos:
            for playlist in all_playlists:
                if video.playlist_id == playlist.playlist_id:
                    correct_playlist = YoutubePlaylist.objects.get(playlist_id=video.playlist_id)
                    correct_playlist.playlist_videos.add(video)

        print("Successfully added to all videos to playlists!")
        print("Repop complete!")
