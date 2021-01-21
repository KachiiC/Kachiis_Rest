import requests
from django.core.management.base import BaseCommand
import json
import os

# Models
from kach_api_endpoints.api_list.youtube_api.youtube_model import YoutubeVideo, YoutubePlaylist
from kach_api_endpoints.management.repoppers.youtube_video_repoppers import create_new_youtube_videos

OUTFILE_LOCATION = os.getcwd() + "/kach_api_endpoints/data/youtube"

DATA_ENDPOINT_URL = "https://www.googleapis.com/youtube/v3/playlistItems?playlistId={}&key=AIzaSyAC-vA8irZClKOO8zVMv4wyF3URfTe6HMA&part=snippet,id&order=date&maxResults=20"


class Command(BaseCommand):

    def handle(self, *args, **options):
        """" Hits the youtube api and returns all playlists in the data folder """

        with open(f"{OUTFILE_LOCATION}/playlistData.json", 'r') as json_file:
            data = json.load(json_file)

        print("Gathering videos from playlist data...")

        for endpoint in data:
            response = requests.get(DATA_ENDPOINT_URL.format(endpoint["playlist_id"])).json()

            with open(f"{OUTFILE_LOCATION}/playlists/{endpoint['playlist_name']}.json", 'w',
                      encoding='utf8') as json_file:
                json_file.write(
                    json.dumps(response, indent=4, ensure_ascii=False)
                )

        print("Successfully gathered playlists")

        YoutubeVideo.objects.all().delete()
        YoutubePlaylist.objects.all().delete()

        with open(f"{OUTFILE_LOCATION}/playlistData.json", 'r') as json_file:
            repop_data = json.load(json_file)

        for file in repop_data:
            create_new_youtube_videos(f"{OUTFILE_LOCATION}/playlists/{file['playlist_name']}.json")

        print("Successfully added videos from playlists!")

        for playlist in repop_data:
            YoutubePlaylist(
                playlist_name=playlist["playlist_name"],
                playlist_id=playlist["playlist_id"]
            ).save()

        print("Successfully created all playlist models")

        all_videos = YoutubeVideo.objects.all()
        all_playlists = YoutubePlaylist.objects.all()

        print("Adding videos to correct playlists...")

        for video in all_videos:
            for playlist in all_playlists:
                if video.playlist_id == playlist.playlist_id:
                    correct_playlist = YoutubePlaylist.objects.get(playlist_id=video.playlist_id)
                    correct_playlist.playlist_videos.add(video)

        print("Successfully added to all videos to playlists!")
        print("Repop complete!")
