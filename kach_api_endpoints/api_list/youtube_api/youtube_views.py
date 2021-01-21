from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .youtube_model import YoutubeVideo, YoutubePlaylist
from .youtube_serializer import YoutubeVideoSerializer, YoutubePlaylistSerializer
from rest_framework.decorators import api_view
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
import requests
import json
import os
from rest_framework import views
# Models
from kach_api_endpoints.api_list.youtube_api.youtube_model import YoutubeVideo, YoutubePlaylist
from kach_api_endpoints.management.repoppers.youtube_video_repoppers import create_new_youtube_videos

OUTFILE_LOCATION = os.getcwd() + "/kach_api_endpoints/data/youtube"

DATA_ENDPOINT_URL = "https://www.googleapis.com/youtube/v3/playlistItems?playlistId={}&key=AIzaSyAC-vA8irZClKOO8zVMv4wyF3URfTe6HMA&part=snippet,id&order=date&maxResults=20"


class YoutubeApiView(views.APIView):

    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, request):
        with open(f"{OUTFILE_LOCATION}/playlistData.json", 'r') as json_file:
            data = json.load(json_file)

        print("Gathering videos from playlist data...")

        for endpoint in data:
            response = requests.get(DATA_ENDPOINT_URL.format(endpoint["playlist_id"])).json()

            with open(f"{OUTFILE_LOCATION}/playlists/{endpoint['playlist_name']}.json", 'w',
                      encoding='utf8') as json_file:
                json_file.write(
                    json.dumps(response, indent=4, ensure_ascii=False)
                )

        print("Successfully gathered playlists")

        YoutubeVideo.objects.all().delete()
        YoutubePlaylist.objects.all().delete()

        with open(f"{OUTFILE_LOCATION}/playlistData.json", 'r') as json_file:
            repop_data = json.load(json_file)

        for file in repop_data:
            create_new_youtube_videos(f"{OUTFILE_LOCATION}/playlists/{file['playlist_name']}.json")

        print("Successfully added videos from playlists!")

        for playlist in repop_data:
            YoutubePlaylist(
                playlist_name=playlist["playlist_name"],
                playlist_id=playlist["playlist_id"]
            ).save()

        print("Successfully created all playlist models")

        all_videos = YoutubeVideo.objects.all()
        all_playlists = YoutubePlaylist.objects.all()

        print("Adding videos to correct playlists...")

        for video in all_videos:
            for playlist in all_playlists:
                if video.playlist_id == playlist.playlist_id:
                    correct_playlist = YoutubePlaylist.objects.get(playlist_id=video.playlist_id)
                    correct_playlist.playlist_videos.add(video)

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


@api_view(['GET', 'POST'])
def youtube_playlist(request):
    if request.method == 'GET':
        data = YoutubePlaylist.objects.all()

        serializer = YoutubePlaylistSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = YoutubePlaylistSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def single_youtube_playlist(request, playlist_id):
    try:
        playlist = YoutubePlaylist.objects.get(playlist_id=playlist_id)
    except YoutubePlaylist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = YoutubePlaylistSerializer(playlist, context={'request': request})

    return Response(serializer.data)
