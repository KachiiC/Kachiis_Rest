from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .music_chart_model import Song
from .music_chart_serializer import SongSerializer


@api_view(['GET', 'POST'])
def chart_list(request):
    if request.method == 'GET':
        data = Song.objects.all()

        serializer = SongSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SongSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
