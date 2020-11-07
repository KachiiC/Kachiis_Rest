from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from kach_api_endpoints.api_list.music_chart_api.music_chart_model import Song
from kach_api_endpoints.api_list.music_chart_api.music_chart_serializer import SongSerializer


class MusicChartTest(APITestCase):
    chart_endpoint = reverse('music_chart')

    song_1 = Song(
        chart_number=1,
        artist="Ariana Grande",
        song_title="Positions"
    )

    song_2 = Song(
        chart_number=2,
        artist="Luke Combs",
        song_title="Forever After All"
    )

    song_3 = Song(
        chart_number=3,
        artist="24kGoldn Featuring iann dior",
        song_title="Mood"
    )

    expected_songs = [song_1, song_2, song_3]

    def setUp(self):
        """Saving songs"""
        for obj in self.expected_songs:
            obj.save()

    def test_retrieve_all_songs(self):
        """retrieve the entire music chart"""
        serializer = SongSerializer(self.expected_songs, many=True)

        response = self.client.get(self.chart_endpoint)

        assert response.status_code == status.HTTP_200_OK
        assert response.data == serializer.data

    def test_retrieve_chart_position(self):
        """"retrieve the chart by chart number"""
        chart_position = reverse('chart_position', args=[self.song_1.chart_number])

        song = Song.objects.get(chart_number=self.song_1.chart_number)

        serializer = SongSerializer(song)

        response = self.client.get(chart_position)

        assert response.status_code == status.HTTP_200_OK
        assert response.data == serializer.data
