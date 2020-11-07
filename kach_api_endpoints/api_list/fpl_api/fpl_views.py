from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .fpl_model import Player
from .fpl_serializers import PlayerSerializer, MatchDaySerializer


@api_view(['GET'])
def players_list(request):
    data = Player.objects.all()

    serializer = PlayerSerializer(data, context={'request': request}, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def player_stats(request, player_id):
    try:
        player = Player.objects.get(player_id=player_id)
    except Player.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = MatchDaySerializer(player, context={'request': request})

    return Response(serializer.data)
