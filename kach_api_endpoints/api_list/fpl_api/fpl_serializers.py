from rest_framework import serializers
from .fpl_model import MatchDay, Player, Chip


class MatchDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchDay
        fields = [
            'gameweek',
            'game_week_points',
            'points_total',
            'team_value',
            'game_week_transfers',
            'game_week_transfers_cost',
            'bench_points',
        ]


class ChipSerializer(serializers.ModelSerializer):
    chip_date = serializers.DateTimeField("%d/%m/%Y")

    class Meta:
        model = Chip
        fields = ["chip_name", "chip_date", "chip_matchday"]


class PlayerSerializer(serializers.ModelSerializer):
    matches = MatchDaySerializer(many=True, read_only=True)
    chips = ChipSerializer(many=True, read_only=True)

    class Meta:
        model = Player
        fields = [
            'player_name',
            'player_id',
            'points_total',
            'transfers_total',
            'points_on_transfers',
            'team_value',
            'current_gameweek',
            'chips',
            'matches',
        ]
