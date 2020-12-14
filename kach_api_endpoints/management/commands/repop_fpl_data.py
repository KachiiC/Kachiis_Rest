import json
import os
from django.core.management.base import BaseCommand
from kach_api_endpoints.api_list.fpl_api.fpl_model import MatchDay, Player
from kach_api_endpoints.management.repoppers.fpl_repoppers import create_fpl_data

FPL_DATA_DIR = os.getcwd() + '/kach_api_endpoints/data/fpl/players/{}Data.json'
LEAGUE_DATA = os.getcwd() + '/kach_api_endpoints/data/fpl/league/leagueData.json'


class Command(BaseCommand):
    def handle(self, *args, **options):
        MatchDay.objects.all().delete()
        Player.objects.all().delete()

        with open(LEAGUE_DATA, 'r') as json_file:
            data = json.load(json_file)

            for player in data["standings"]["results"]:
                create_fpl_data(FPL_DATA_DIR.format(player["entry"]))

        match_days = MatchDay.objects.all()
        players_list = Player.objects.all()

        for match in match_days:
            for player in players_list:
                if match.player_id == player.player_id:
                    correct_player = Player.objects.get(player_id=match.player_id)
                    correct_player.matches.add(match)

        print("repop successful!")