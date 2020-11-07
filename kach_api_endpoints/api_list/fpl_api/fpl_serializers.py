from rest_framework import serializers
from .fpl_model import MatchDay, Player


class MatchDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchDay
        fields = ('player_id', 'gameweek', 'game_week_points', 'points_total', 'team_value',
                  'game_week_transfers', 'game_week_transfers_cost', 'bench_points')


class PlayerSerializer(serializers.ModelSerializer):
    matches = MatchDaySerializer(many=True, read_only=True)

    class Meta:
        model = Player
        fields = ('pk', 'player_name', 'player_id', 'matches')
