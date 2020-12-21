from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from kach_api_endpoints.api_list.fpl_api.fpl_model import Player, MatchDay
from kach_api_endpoints.api_list.fpl_api.fpl_serializers import PlayerSerializer, MatchDaySerializer


class FplTest(APITestCase):
    fpl_endpoint = reverse("fpl_players")

    match_day_1 = MatchDay(
        player_id=2341747,
        gameweek=1,
        game_week_points=60,
        points_total=60,
        team_value=1000,
        game_week_transfers=0,
        game_week_transfers_cost=0,
        bench_points=6
    )

    match_day_2 = MatchDay(
        player_id=2341747,
        gameweek=2,
        game_week_points=79,
        points_total=139,
        team_value=1000,
        game_week_transfers=1,
        game_week_transfers_cost=0,
        bench_points=3
    )

    match_day_3 = MatchDay(
        player_id=684633,
        gameweek=1,
        game_week_points=75,
        points_total=75,
        team_value=1000,
        game_week_transfers=0,
        game_week_transfers_cost=0,
        bench_points=3
    )

    player_1 = Player(
        player_name="Anthony",
        player_id=2341747,
        points_total=200,
        transfers_total=5,
        current_gameweek=3,
    )

    player_2 = Player(
        player_name="Kacheok",
        player_id=684633,
        points_total=250,
        transfers_total=7,
        current_gameweek=3,
    )

    expected_matches = [match_day_1, match_day_2, match_day_3]
    expected_players = [player_1, player_2]

    def setUp(self):
        for obj in self.expected_players:
            obj.save()

        for obj in self.expected_matches:
            obj.save()

    def test_add_match_to_player(self):
        """test adding match to players"""
        match_days = MatchDay.objects.all()
        players_list = Player.objects.all()

        for match in match_days:
            for player in players_list:
                if match.player_id == player.player_id:
                    correct_player = Player.objects.get(player_id=match.player_id)
                    correct_player.matches.add(match)

        anthony = Player.objects.get(player_name="Anthony")
        kacheok = Player.objects.get(player_name="Kacheok")

        assert anthony.matches.count() == 2
        assert kacheok.matches.count() == 1

    def test_get_all_players(self):
        """"Test getting all players"""
        serializer = PlayerSerializer(self.expected_players, many=True)

        response = self.client.get(self.fpl_endpoint)
        assert response.status_code == status.HTTP_200_OK
        assert response.data == serializer.data
