import requests
from django.core.management.base import BaseCommand
import json
import os

OUTFILE_LOCATION = os.getcwd() + "/kach_api_endpoints/data/fpl"

DATA_ENDPOINTS = [
    {"playerId": "34170", "output": "faraData"},
    {"playerId": "684633", "output": "kachData"},
    {"playerId": "158159", "output": "danData"},
    {"playerId": "2341747", "output": "antData"},
    {"playerId": "979495", "output": "rickyData"},
    {"playerId": "1029246", "output": "zeenData"},
    {"playerId": "4316712", "output": "shirleyData"},
    {"playerId": "1867039", "output": "michaelData"},
    {"playerId": "213553", "output": "elijhaData"},
    {"playerId": "1639999", "output": "haydenData"},
]

MATCH_ENDPOINT_URL = "https://fantasy.premierleague.com/api/entry/{}/history/"
PLAYER_ENDPOINT_URL = "https://fantasy.premierleague.com/api/entry/{}/"


class Command(BaseCommand):

    def handle(self, *args, **options):
        for endpoint in DATA_ENDPOINTS:
            match_response = requests.get(MATCH_ENDPOINT_URL.format(endpoint["playerId"])).json()
            player_response = requests.get(PLAYER_ENDPOINT_URL.format(endpoint["playerId"])).json()

            with open(f"{OUTFILE_LOCATION}/{endpoint['output']}.json", 'w', encoding='utf8') as json_file:
                json_file.write(
                    json.dumps((match_response, player_response), indent=4, ensure_ascii=False)
                )

            print(f"successfully prepped {endpoint['output']}.json")
