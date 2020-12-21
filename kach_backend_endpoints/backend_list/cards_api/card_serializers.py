from rest_framework import serializers
from .card_model import Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('code', 'value', 'image', 'suit')
