import requests
from django.core.management.base import BaseCommand
import json
import os

OUTFILE_LOCATION = os.getcwd() + "/kach_api_endpoints/data/youtube"

DATA_ENDPOINT_URL = "https://www.googleapis.com/youtube/v3/playlistItems?playlistId={}&key=AIzaSyAC-vA8irZClKOO8zVMv4wyF3URfTe6HMA&part=snippet,id&order=date&maxResults=20"

DATA_ENDPOINTS = [
    # Insert playlistId and name the output file
    {
        "playlistId": "PLaaEeFtNlIJ1QCSWkBvxItbKYEpGENASC",
        "output": "ufcFightsData",
    },
    {
        "playlistId": "PLaaEeFtNlIJ2Yigy4wHCQlcuRZg4NKbi5",
        "output": "fightHighlightsData",
    },
]


class Command(BaseCommand):

    def handle(self, *args, **options):
        """" Hits the youtube api and returns all playlists in the data folder """
        for endpoint in DATA_ENDPOINTS:
            response = requests.get(DATA_ENDPOINT_URL.format(endpoint["playlistId"])).json()

            with open(f"{OUTFILE_LOCATION}/{endpoint['output']}.json", 'w', encoding='utf8') as json_file:
                json_file.write(
                    json.dumps(response, indent=4, ensure_ascii=False)
                )

            print(f"successfully prepped {endpoint['output']}.json")
