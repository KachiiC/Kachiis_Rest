import random
from rest_framework import views
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .mma_fighter_model import Fighter
from .mma_fighter_serializer import FighterSerializer


@api_view(['GET'])
def mma_fighter_list(request):
    data = Fighter.objects.all()

    serializer = FighterSerializer(data, context={'request': request}, many=True)

    return Response(serializer.data)


class FeaturedFighterApiView(views.APIView):

    @method_decorator(cache_page(60 * 60 * 24))
    def get(self, request):
        all_fighters = Fighter.objects.all()

        random_fighter = random.choice(all_fighters)

        serializer = FighterSerializer(random_fighter, context={'request': request})

        return Response(serializer.data)
