from rest_framework import serializers
from kach_backend_endpoints.backend_list.mma_fighters.mma_fighter_model import Fighter
from kach_backend_endpoints.backend_list.mma_fights.mma_fights_model import Fight


class CornerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fighter
        fields = [
            "first_name",
            "last_name",
            "nickname",
            "date_of_birth",
            "height",
            "reach",
            "wins",
            "losses",
            "draws",
            "no_contests"
        ]


class FightSerializer(serializers.ModelSerializer):
    red_corner = CornerSerializer(read_only=True)
    blue_corner = CornerSerializer(read_only=True)

    class Meta:
        model = Fight
        fields = [
            "red_corner",
            "blue_corner",
            "winner",
            "method_of_victory",
            "round",
            "draw",
            "weight_class",
            "title_fight",
            "video",
            "event",
            "date",
            "notable_win"
        ]
