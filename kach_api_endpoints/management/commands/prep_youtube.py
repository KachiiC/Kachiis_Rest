import requests
from django.core.management.base import BaseCommand
import json
import os

OUTFILE_LOCATION = os.getcwd() + "/kach_api_endpoints/data/youtube"

DATA_ENDPOINT_URL = "https://www.googleapis.com/youtube/v3/playlistItems?playlistId={}&key=AIzaSyAC-vA8irZClKOO8zVMv4wyF3URfTe6HMA&part=snippet,id&order=date&maxResults=20"


class Command(BaseCommand):

    def handle(self, *args, **options):
        """" Hits the youtube api and returns all playlists in the data folder """

        with open(f"{OUTFILE_LOCATION}/playlistData.json", 'r') as json_file:
            data = json.load(json_file)

            for endpoint in data:
                response = requests.get(DATA_ENDPOINT_URL.format(endpoint["playlist_id"])).json()

                with open(f"{OUTFILE_LOCATION}/playlists/{endpoint['playlist_name']}.json", 'w',
                          encoding='utf8') as json_file:
                    json_file.write(
                        json.dumps(response, indent=4, ensure_ascii=False)
                    )

                print(f"successfully prepped {endpoint['playlist_name']}.json")
