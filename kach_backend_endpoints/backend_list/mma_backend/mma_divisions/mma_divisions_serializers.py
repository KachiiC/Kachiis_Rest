from rest_framework import serializers
from kach_backend_endpoints.backend_list.mma_backend.mma_fighters.mma_fighter_serializer import FighterSerializer
from .mma_divisions_model import Division


class MMADivisionSerializer(serializers.ModelSerializer):
    fighters = FighterSerializer(many=True, read_only=True)

    class Meta:
        model = Division
        fields = [
            "weight_class",
            "gender",
            "fighters"
        ]
