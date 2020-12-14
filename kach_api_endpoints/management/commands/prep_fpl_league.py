import requests
from django.core.management.base import BaseCommand
import json
import os

OUTFILE_LOCATION = os.getcwd() + "/kach_api_endpoints/data/fpl/league"

LEAGUE_ENDPOINT_URL = "https://fantasy.premierleague.com/api/leagues-classic/{}/standings/"

league_id = 357383  # Insert League Id HERE


class Command(BaseCommand):

    def handle(self, *args, **options):
        league_response = requests.get(LEAGUE_ENDPOINT_URL.format(league_id)).json()

        with open(f"{OUTFILE_LOCATION}/leagueData.json", 'w', encoding='utf8') as json_file:
            json_file.write(
                json.dumps(league_response, indent=4, ensure_ascii=False)
            )

        print(f"successfully prepped leagueData.json")
