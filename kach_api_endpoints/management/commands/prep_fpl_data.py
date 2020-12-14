import requests
from django.core.management.base import BaseCommand
import json
import os

OUTFILE_LOCATION = os.getcwd() + "/kach_api_endpoints/data/fpl/players"

LEAGUE_DATA = os.getcwd() + "/kach_api_endpoints/data/fpl/league/leagueData.json"

MATCH_ENDPOINT_URL = "https://fantasy.premierleague.com/api/entry/{}/history/"

PLAYER_ENDPOINT_URL = "https://fantasy.premierleague.com/api/entry/{}/"


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open(LEAGUE_DATA, 'r') as json_file:
            data = json.load(json_file)

            for player in data["standings"]["results"]:
                match_response = requests.get(MATCH_ENDPOINT_URL.format(player["entry"])).json()
                player_response = requests.get(PLAYER_ENDPOINT_URL.format(player["entry"])).json()

                with open(f"{OUTFILE_LOCATION}/{player['entry']}Data.json", 'w', encoding='utf8') as json_file:
                    json_file.write(
                        json.dumps((match_response, player_response), indent=4, ensure_ascii=False)
                    )

                print(f"successfully prepped {player['entry']}.json")