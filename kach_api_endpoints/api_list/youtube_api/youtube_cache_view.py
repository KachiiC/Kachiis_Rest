import os
import json
import requests
import random
from kach_api_endpoints.management.repoppers.youtube_video_repoppers import create_new_youtube_videos
from rest_framework import views
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .youtube_serializer import YoutubeVideoSerializer
from .youtube_model import YoutubeVideo, YoutubePlaylist

OUTFILE_LOCATION = os.getcwd() + "/kach_api_endpoints/data/youtube/cache_playlist/playlistData.json"

DATA_ENDPOINT_URL = "https://www.googleapis.com/youtube/v3/playlistItems?playlistId" \
                    "=PLaaEeFtNlIJ2Yigy4wHCQlcuRZg4NKbi5&key=AIzaSyAC-vA8irZClKOO8zVMv4wyF3URfTe6HMA&part=snippet," \
                    "id&order=date&maxResults=20 "


class YoutubeApiView(views.APIView):

    @method_decorator(cache_page(60 * 60 * 24 * 7))
    def get(self, request):
        response = requests.get(DATA_ENDPOINT_URL).json()

        with open(OUTFILE_LOCATION, 'w',
                  encoding='utf8') as json_file:
            json_file.write(
                json.dumps(response, indent=4, ensure_ascii=False)
            )

        YoutubeVideo.objects.all().delete()
        YoutubePlaylist.objects.all().delete()

        create_new_youtube_videos(OUTFILE_LOCATION)

        data = YoutubeVideo.objects.all()

        serializer = YoutubeVideoSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)


class YoutubeFeaturedVideoApiView(views.APIView):
    @method_decorator(cache_page(60 * 60 * 24))
    def get(self, request):
        playlist_videos = YoutubeVideo.objects.filter(playlist_name="ufc_fights")
        random_video = random.choice(playlist_videos)

        serializer = YoutubeVideoSerializer(random_video, context={'request': request})

        return Response(serializer.data)
