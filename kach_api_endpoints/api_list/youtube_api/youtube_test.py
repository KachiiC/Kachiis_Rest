from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from kach_api_endpoints.api_list.youtube_api.youtube_model import YoutubeVideo, YoutubePlaylist
from kach_api_endpoints.api_list.youtube_api.youtube_serializer import YoutubeVideoSerializer, YoutubePlaylistSerializer


class MMAVideosTest(APITestCase):
    videos_endpoint = reverse('youtube_videos')
    playlist_endpoint = reverse('youtube_playlists')

    youtube_video_1 = YoutubeVideo(
        video_title="Robert Whittaker v Jared Cannonier | UFC 254 Highlights",
        video_id="kyhgMr0J36o",
        video_description="Robert Whittaker gets another impressive win on his second visit to UFC Fight Island",
        upload_date="2020-10-27T01:07:30Z",
        video_thumbnail="https://i.ytimg.com/vi/kyhgMr0J36o/maxresdefault.jpg",
        playlist_id="PLaaEeFtNlIJ2Yigy4wHCQlcuRZg4NKbi5",
        channel_id="UCGFG6QjQru4YRlBfZ1HqNFA"
    )

    youtube_video_2 = YoutubeVideo(
        video_title="Khabib Nurmagomedov v Justin Gaethje | UFC 254 fight highlights",
        video_id="MyI8AsqLWPI",
        video_description="Khabib Nurmagomedov bows out from the UFC following his legacy defining win",
        upload_date="2020-10-27T01:07:37Z",
        video_thumbnail="https://i.ytimg.com/vi/MyI8AsqLWPI/maxresdefault.jpg",
        playlist_id="PLaaEeFtNlIJ2Yigy4wHCQlcuRZg4NKbi5",
        channel_id="UCGFG6QjQru4YRlBfZ1HqNFA"
    )

    youtube_video_3 = YoutubeVideo(
        video_title="Free Fight: Jon Jones vs Alexander Gustafsson 1 | UFC 165,  2013",
        video_id="en4hR34Bl8w",
        video_description="Relive one of the most entertaining bouts in Jon Jones career so far",
        upload_date="2020-06-27T16:15:14Z",
        video_thumbnail="https://i.ytimg.com/vi/en4hR34Bl8w/maxresdefault.jpg",
        playlist_id="PLaaEeFtNlIJ1QCSWkBvxItbKYEpGENASC",
        channel_id="UCGFG6QjQru4YRlBfZ1HqNFA"
    )

    youtube_playlist_1 = YoutubePlaylist(
        playlist_name="UFC Fights",
        playlist_id="PLaaEeFtNlIJ1QCSWkBvxItbKYEpGENASC"
    )

    youtube_playlist_2 = YoutubePlaylist(
        playlist_name="Fight Highlights",
        playlist_id="PLaaEeFtNlIJ2Yigy4wHCQlcuRZg4NKbi5"
    )



    def setUp(self):
        """Saving videos and playlists"""
        for obj in self.expected_videos:
            obj.save()

        for obj in self.expected_playlists:
            obj.save()


    def test_retrieve_all_videos(self):
        """"Retrieve all videos"""
        serializer = YoutubeVideoSerializer(self.expected_videos, many=True)

        response = self.client.get(self.videos_endpoint)
        assert response.status_code == status.HTTP_200_OK
        assert response.data == serializer.data

    def test_retrieve_single_video(self):
        """" Retrieve a single playlist"""
        single_playlist = reverse('single_youtube_playlist', args=[self.youtube_playlist_1.playlist_id])

        video = YoutubePlaylist.objects.get(playlist_id=self.youtube_playlist_1.playlist_id)

        serializer = YoutubePlaylistSerializer(video)

        response = self.client.get(single_playlist)

        assert response.status_code == status.HTTP_200_OK
        assert response.data == serializer.data

    def test_adding_to_playlist(self):
        """ Testing saving videos to playlist depending on playlist_video_id"""

        all_videos = YoutubeVideo.objects.all()
        all_playlists = YoutubePlaylist.objects.all()

        for video in all_videos:
            for playlist in all_playlists:
                if video.playlist_id == playlist.playlist_id:
                    correct_playlist = YoutubePlaylist.objects.get(playlist_id=video.playlist_id)
                    correct_playlist.playlist_videos.add(video)

        ufc_fights = YoutubePlaylist.objects.get(playlist_name="UFC Fights")
        fight_highlights = YoutubePlaylist.objects.get(playlist_name="Fight Highlights")

        assert ufc_fights.playlist_videos.count() == 1
        assert fight_highlights.playlist_videos.count() == 2

    def test_retrieve_all_playlists(self):
        """ Retrieve all existing playlists"""

        serializer = YoutubePlaylistSerializer(self.expected_playlists, many=True)

        response = self.client.get(self.playlist_endpoint)
        assert response.status_code == status.HTTP_200_OK
        assert response.data == serializer.data

    def test_retrieve_single_playlist(self):
        """" Retrieve a single playlist"""
        single_playlist = reverse('single_youtube_playlist', args=[self.youtube_playlist_1.playlist_id])

        video = YoutubePlaylist.objects.get(playlist_id=self.youtube_playlist_1.playlist_id)

        serializer = YoutubePlaylistSerializer(video)

        response = self.client.get(single_playlist)

        assert response.status_code == status.HTTP_200_OK
        assert response.data == serializer.data
