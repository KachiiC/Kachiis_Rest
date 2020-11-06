import requests
from django.core.management.base import BaseCommand
import json
import os

OUTFILE_LOCATION = os.getcwd() + "/kach_api_endpoints/data/music_charts"

url = "https://billboard-charts.p.rapidapi.com/billboard/v1/showchart"

querystring = {"chart": "hot-100"}

headers = {
    'x-rapidapi-key': "985371e109mshb5666c0424d5dcfp1b7485jsndf2afe5a3591",
    'x-rapidapi-host': "billboard-charts.p.rapidapi.com"
}


class Command(BaseCommand):

    def handle(self, *args, **options):
        """" Hits the billboard 100 api and returns all charter songs in the data folder """
        response = requests.request("GET", url, headers=headers, params=querystring).json()

        with open(f"{OUTFILE_LOCATION}/music_charts.json", 'w', encoding='utf8') as json_file:
            json_file.write(
                json.dumps(response, indent=4, ensure_ascii=False)
            )

        print(f"successfully prepped musicCharts.json")