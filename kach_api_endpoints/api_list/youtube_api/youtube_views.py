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
