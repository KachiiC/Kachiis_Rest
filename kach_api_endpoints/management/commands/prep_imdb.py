import requests
from django.core.management.base import BaseCommand
import json
import os

OUTFILE_LOCATION = os.getcwd() + "/kach_api_endpoints/data/fpl"

url = "https://movies-tvshows-data-imdb.p.rapidapi.com/"

headers = {
    'x-rapidapi-key': "985371e109mshb5666c0424d5dcfp1b7485jsndf2afe5a3591",
    'x-rapidapi-host': "movies-tvshows-data-imdb.p.rapidapi.com"
}

ENDPOINTS = [
    {"name": "trendingShows", "type": "get-trending-shows", "page": "1"},
    {"name": "trendingMovies", "type": "get-trending-movies", "page": "1"},
    {"name": "popularShows", "type": "get-popular-shows", "year": "2020", "page": "1"},
    {"name": "popularMovies", "type": "get-popular-movies", "year": "2020", "page": "1"},
]


class Command(BaseCommand):
    def handle(self, *args, **options):
        for endpoint in ENDPOINTS:
            response = requests.request("GET", url, headers=headers, params=endpoint).json()

            with open(f"{OUTFILE_LOCATION}/{endpoint['name']}.json", 'w', encoding='utf8') as json_file:
                json_file.write(
                    json.dumps(response, indent=4, ensure_ascii=False)
                )

            print(f"successfully prepped {endpoint['name']}.json")
