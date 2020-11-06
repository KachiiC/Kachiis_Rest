from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .youtube_model import YoutubeVideo, YoutubePlaylist
from .youtube_serializer import YoutubeVideoSerializer, YoutubePlaylistSerializer


@api_view(['GET', 'POST'])
def youtube_videos_list(request):
    if request.method == 'GET':
        data = YoutubeVideo.objects.all()

        serializer = YoutubeVideoSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = YoutubeVideoSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
