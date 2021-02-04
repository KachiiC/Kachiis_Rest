from rest_framework import serializers
from .mma_fighter_model import Fighter
from kach_backend_endpoints.backend_list.mma_fights.mma_fights_model import Fight


class WinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fight
        fields = [
            "red_corner",
            "blue_corner",
            "method_of_victory",
            "round",
            "weight_class",
            "title_fight",
            "video",
            "event",
            "date",
        ]


class FighterSerializer(serializers.ModelSerializer):
    # notable_wins = WinSerializer(many=True, read_only=True)

    class Meta:
        model = Fighter
        fields = [
            "first_name",
            "last_name",
            "rank",
            "is_champion",
            "weight_class",
            # "nickname",
            # "status",
            # "date_of_birth",
            # "promotion",
            # "rank",
            # "height",
            # "reach",
            # "style",
            # "wins",
            # "losses",
            # "draws",
            # "no_contests",
            # "wins_via_knockout",
            # "wins_via_submission",
            # "wins_via_decision",
            # "losses_via_knockout",
            # "losses_via_submission",
            # "losses_via_decision",
            # "notable_wins",
        ]
