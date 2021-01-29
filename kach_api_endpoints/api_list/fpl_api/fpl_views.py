from rest_framework.decorators import api_view
from rest_framework import status
from .fpl_model import Player, MatchDay, Chip
from .fpl_serializers import PlayerSerializer, MatchDaySerializer
import requests
import json
import os
from kach_api_endpoints.management.repoppers.fpl_repoppers import create_fpl_data
from rest_framework import views
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

league_id = 357383  # Insert League Id HERE

OUTFILE_LOCATION = os.getcwd() + "/kach_api_endpoints/data/fpl/"

ENDPOINT_URL = "https://fantasy.premierleague.com/api"


class FplApiView(views.APIView):

    @method_decorator(cache_page(60 * 60 * 6))
    def get(self, request):
        league_response = requests.get(f"{ENDPOINT_URL}/leagues-classic/{league_id}/standings/").json()

        with open(f"{OUTFILE_LOCATION}league/leagueData.json", 'w', encoding='utf8') as json_file:
            json_file.write(json.dumps(league_response, indent=4, ensure_ascii=False))

        print(f"Successfully prepped leagueData.json")

        with open(f"{OUTFILE_LOCATION}league/leagueData.json", 'r') as json_file:
            data = json.load(json_file)

            print("prepping players data...")

            for player in data["standings"]["results"]:
                match_response = requests.get(f"{ENDPOINT_URL}/entry/{player['entry']}/history/").json()

                player_response = requests.get(f"{ENDPOINT_URL}/entry/{player['entry']}/").json()

                with open(f"{OUTFILE_LOCATION}/players/{player['entry']}Data.json", 'w', encoding='utf8') as json_file:
                    json_file.write(json.dumps((match_response, player_response), indent=4, ensure_ascii=False))

        print("Successfully prepped players data!")

        MatchDay.objects.all().delete()
        Player.objects.all().delete()
        Chip.objects.all().delete()

        print("Repopping player and match data...")

        with open(f"{OUTFILE_LOCATION}league/leagueData.json", 'r') as json_file:
            data = json.load(json_file)

            for player in data["standings"]["results"]:
                create_fpl_data(f"{OUTFILE_LOCATION}players/{player['entry']}Data.json")

        match_days = MatchDay.objects.all()
        players_list = Player.objects.all()
        all_chips = Chip.objects.all()

        for match in match_days:
            for player in players_list:
                if match.player_id == player.player_id:
                    correct_player = Player.objects.get(player_id=match.player_id)
                    correct_player.matches.add(match)

        for chip in all_chips:
            for player in players_list:
                if chip.chip_owner == player.player_name:
                    correct_player = Player.objects.get(player_name=chip.chip_owner)
                    correct_player.chips.add(chip)

        serializer = PlayerSerializer(players_list, context={'request': request}, many=True)

        return Response(serializer.data)


@api_view(['GET'])
def players_list(request):
    data = Player.objects.all()

    serializer = PlayerSerializer(data, context={'request': request}, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def player_stats(request, player_name):
    try:
        player = Player.objects.get(player_name=player_name.capitalize())
    except Player.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PlayerSerializer(player, context={'request': request})

    return Response(serializer.data)


@api_view(['GET'])
def match_day_list(request):
    data = MatchDay.objects.all()

    serializer = MatchDaySerializer(data, context={'request': request}, many=True)

    return Response(serializer.data)
