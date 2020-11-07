from rest_framework import serializers
from .music_chart_model import Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ("chart_number", "artist", "song_title")
