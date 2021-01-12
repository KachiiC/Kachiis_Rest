from rest_framework import serializers
from .mma_fighter_model import Fighter


class FighterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fighter
        fields = [
            "first_name",
            "last_name",
            "nickname",
            "status",
            "date_of_birth",
            "promotion",
            "rank",
            "height",
            "reach",
            "weight_class",
            "style",
            "notable_wins",
            "wins",
            "losses",
            "draws",
            "no_contests",
            "wins_via_knockout",
            "wins_via_submission",
            "wins_via_decision",
            "losses_via_knockout",
            "losses_via_submission",
            "losses_via_decision"
        ]
