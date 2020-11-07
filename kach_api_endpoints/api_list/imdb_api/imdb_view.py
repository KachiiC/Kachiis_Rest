from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .imdb_model import ImdbList
from .imdb_serializer import ImdbListSerializer


@api_view(['GET'])
def imdb_lists(request):
    data = ImdbList.objects.all()

    serializer = ImdbListSerializer(data, context={'request': request}, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def single_imdb_list(request, chart_number):
    try:
        chart_song = ImdbList.objects.get(chart_number=chart_number)
    except ImdbList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ImdbListSerializer(chart_song, context={'request': request})

    return Response(serializer.data)
