import os
from django.core.management.base import BaseCommand
from kach_api_endpoints.api_list.fpl_api.fpl_model import MatchDay, Player
from kach_api_endpoints.management.repoppers.fpl_repoppers import create_fpl_data

FPL_DATA_DIR = os.getcwd() + '/kach_api_endpoints/data/fpl/{}Data.json'

players = ["ant", "dan", "elijha", "fara", "hayden", "kach", "michael", "ricky", "shirley", "zeen"]


class Command(BaseCommand):
    def handle(self, *args, **options):
        MatchDay.objects.all().delete()
        Player.objects.all().delete()

        for player in players:
            create_fpl_data(FPL_DATA_DIR.format(player))

        match_days = MatchDay.objects.all()
        players_list = Player.objects.all()

        for match in match_days:
            for player in players_list:
                if match.player_id == player.player_id:
                    correct_player = Player.objects.get(player_id=match.player_id)
                    correct_player.matches.add(match)

        print("repop successful!")
