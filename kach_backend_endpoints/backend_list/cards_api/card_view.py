from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .card_model import Card
from .card_serializers import CardSerializer


@api_view(['GET', 'POST'])
def cards_list(request):
    if request.method == 'GET':
        data = Card.objects.all()

        serializer = CardSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CardSerializer(data=request.data, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)