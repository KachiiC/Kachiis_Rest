from rest_framework.response import Response
from rest_framework.decorators import api_view
from .mma_divisions_model import Division
from .mma_divisions_serializers import MMADivisionSerializer


@api_view(['GET'])
def mma_divisions_list(request):
    data = Division.objects.all()

    serializer = MMADivisionSerializer(data, context={'request': request}, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def mma_mens_p4p(request):
    data = Division.objects.get(weight_class="Men's Pound-for-Pound Top Rank")

    serializer = MMADivisionSerializer(data, context={'request': request})

    return Response(serializer.data)


@api_view(['GET'])
def mma_womens_p4p(request):
    data = Division.objects.get(weight_class="Women's Pound-for-Pound Top Rank")

    serializer = MMADivisionSerializer(data, context={'request': request})

    return Response(serializer.data)
