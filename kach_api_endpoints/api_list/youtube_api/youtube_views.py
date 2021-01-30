import os
import json
import requests
import random
from kach_api_endpoints.management.repoppers.youtube_video_repoppers import create_new_youtube_videos
from rest_framework import views
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .youtube_serializer import YoutubeVideoSerializer, YoutubePlaylistSerializer
from .youtube_model import YoutubeVideo, YoutubePlaylist

OUTFILE_LOCATION = os.getcwd() + "/kach_api_endpoints/data/youtube"

DATA_ENDPOINT_URL = "https://www.googleapis.com/youtube/v3/playlistItems?playlistId={" \
                    "}&key=AIzaSyAC-vA8irZClKOO8zVMv4wyF3URfTe6HMA&part=snippet,id&order=date&maxResults=20"


class YoutubeApiView(views.APIView):

    @method_decorator(cache_page(60 * 60 * 24 * 7))
    def get(self, request):
        with open(f"{OUTFILE_LOCATION}/playlistData.json", 'r') as json_file:
            data = json.load(json_file)

        for endpoint in data:
            response = requests.get(DATA_ENDPOINT_URL.format(endpoint["playlist_id"])).json()

            with open(f"{OUTFILE_LOCATION}/playlists/{endpoint['playlist_name']}.json", 'w',
                      encoding='utf8') as json_file:
                json_file.write(
                    json.dumps(response, indent=4, ensure_ascii=False)
                )

        YoutubeVideo.objects.all().delete()
        YoutubePlaylist.objects.all().delete()

        with open(f"{OUTFILE_LOCATION}/playlistData.json", 'r') as json_file:
            repop_data = json.load(json_file)

        for file in repop_data:
            create_new_youtube_videos(f"{OUTFILE_LOCATION}/playlists/{file['playlist_name']}.json")

        for playlist in repop_data:
            YoutubePlaylist(
                playlist_name=playlist["playlist_name"],
                playlist_id=playlist["playlist_id"]
            ).save()

        all_videos = YoutubeVideo.objects.all()
        all_playlists = YoutubePlaylist.objects.all()

        for video in all_videos:
            for playlist in all_playlists:
                if video.playlist_id == playlist.playlist_id:
                    correct_playlist = YoutubePlaylist.objects.get(playlist_id=video.playlist_id)
                    correct_playlist.playlist_videos.add(video)

        data = YoutubeVideo.objects.all()

        serializer = YoutubeVideoSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)


@api_view(['GET'])
def youtube_videos_list(request):
    if request.method == 'GET':
        data = YoutubeVideo.objects.all()

        serializer = YoutubeVideoSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)


@api_view(['GET'])
def single_youtube_video(request, video_id):
    try:
        playlist = YoutubeVideo.objects.get(video_id=video_id)
    except YoutubeVideo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = YoutubeVideoSerializer(playlist, context={'request': request})

    return Response(serializer.data)


@api_view(['GET'])
def youtube_playlist(request):
    if request.method == 'GET':
        data = YoutubePlaylist.objects.all()

        serializer = YoutubePlaylistSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)


@api_view(['GET'])
def single_youtube_playlist(request, playlist_id):
    try:
        playlist = YoutubePlaylist.objects.get(playlist_id=playlist_id)
    except YoutubePlaylist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = YoutubePlaylistSerializer(playlist, context={'request': request})

    return Response(serializer.data)


class YoutubeFeaturedVideoApiView(views.APIView):
    @method_decorator(cache_page(60 * 60 * 24))
    def get(self, request):
        playlist_videos = YoutubeVideo.objects.all()
        random_video = random.choice(playlist_videos)

        serializer = YoutubeVideoSerializer(random_video, context={'request': request})

        return Response(serializer.data)
