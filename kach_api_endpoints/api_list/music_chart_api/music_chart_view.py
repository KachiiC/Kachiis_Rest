from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .music_chart_model import Song
from .music_chart_serializer import SongSerializer


@api_view(['GET'])
def chart_list(request):
    data = Song.objects.all()

    serializer = SongSerializer(data, context={'request': request}, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def chart_position(request, chart_number):
    try:
        chart_song = Song.objects.get(chart_number=chart_number)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = SongSerializer(chart_song, context={'request': request})

    return Response(serializer.data)
