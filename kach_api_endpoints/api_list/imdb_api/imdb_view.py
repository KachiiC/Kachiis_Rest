from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .imdb_model import ImdbList, Content
from .imdb_serializer import ImdbListSerializer, ContentSerializer


@api_view(['GET'])
def imdb_lists(request):
    data = ImdbList.objects.all()

    serializer = ImdbListSerializer(data, context={'request': request}, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def single_imdb_list(request, content_type):
    try:
        single_list = ImdbList.objects.get(content_type=content_type)
    except ImdbList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ImdbListSerializer(single_list, context={'request': request})

    return Response(serializer.data)


@api_view(['GET'])
def content_list(request):
    data = Content.objects.all()

    serializer = ContentSerializer(data, context={'request': request}, many=True)

    return Response(serializer.data)
