from rest_framework import serializers
from .mma_fights_model import Fight


class FightSerializer(serializers.ModelSerializer):
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
