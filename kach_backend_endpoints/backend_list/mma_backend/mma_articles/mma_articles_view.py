from rest_framework.response import Response
from rest_framework.decorators import api_view
from .mma_articles_model import Article
from .mma_articles_serializer import ArticleSerializer


@api_view(['GET'])
def mma_articles_list(request):
    data = Article.objects.all()

    serializer = ArticleSerializer(data, context={'request': request}, many=True)

    return Response(serializer.data)
