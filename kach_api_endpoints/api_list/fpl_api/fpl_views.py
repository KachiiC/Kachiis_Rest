import os
import requests
import json
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import views
from rest_framework.response import Response
from .fpl_model import Player, MatchDay
from .fpl_serializers import PlayerSerializer, MatchDaySerializer
from .fpl_cache_view import fpl_cache_function

league_id = 357383  # Insert League Id HERE


class FplApiView(views.APIView):

    @method_decorator(cache_page(60 * 60 * 3))
    def get(self, request):
        fpl_cache_function(league_id)

        serializer = PlayerSerializer(players_list, context={'request': request}, many=True)

        return Response(serializer.data)


class FplSearchApiView(views.APIView):

    @method_decorator(cache_page(60 * 5))
    def get(self, request, input_league_id):
        fpl_cache_function(input_league_id)

        serializer = PlayerSerializer(players_list, context={'request': request}, many=True)

        return Response(serializer.data)


@api_view(['GET'])
def players_list(request):
    data = Player.objects.all()

    serializer = PlayerSerializer(data, context={'request': request}, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def player_stats(request, player_name):
    try:
        player = Player.objects.get(player_name=player_name.capitalize())
    except Player.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PlayerSerializer(player, context={'request': request})

    return Response(serializer.data)


@api_view(['GET'])
def match_day_list(request):
    data = MatchDay.objects.all()

    serializer = MatchDaySerializer(data, context={'request': request}, many=True)

    return Response(serializer.data)
