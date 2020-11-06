from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from kach_api_endpoints.api_list.music_chart_api.music_chart_model import Song
from kach_api_endpoints.api_list.music_chart_api.music_chart_serializer import SongSerializer


class MusicChartTest(APITestCase):
    chart_endpoint = reverse('music_chart')

    song_1 = Song(
        chart_position=1,
        artist="Ariana Grande",
        song_title="Positions"
    )
