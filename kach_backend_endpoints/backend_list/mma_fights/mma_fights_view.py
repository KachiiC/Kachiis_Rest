from rest_framework.response import Response

from rest_framework.decorators import api_view
from .mma_fights_model import Fight
from .mma_fights_serializer import FightSerializer


@api_view(['GET'])
def mma_fights_list(request):
    data = Fight.objects.all()

    serializer = FightSerializer(data, context={'request': request}, many=True)

    return Response(serializer.data)
