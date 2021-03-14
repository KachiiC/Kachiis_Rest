from rest_framework import serializers
# My Models
from .mma_techniques_model import Technique


class TechniquesSerializer(serializers.ModelSerializer):  # MMA News

    class Meta:
        model = Technique
        fields = ['title', 'type', 'discipline', 'difficulty', 'description', 'tutorial', 'mistakes']
