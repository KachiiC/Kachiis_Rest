from rest_framework import views
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .mma_articles_model import Article
from kach_backend_endpoints.management.url_webscrapper_lite import url_webscraper_lite
from .mma_articles_serializer import ArticleSerializer
from rest_framework.response import Response

my_url = "https://www.mmaweekly.com/category/news"


class MMAArticlesView(views.APIView):

    @method_decorator(cache_page(60 * 60 * 24))
    def get(self, request):
        # Delete all objects
        Article.objects.all().delete()

        # Grabs Articles
        page = url_webscraper_lite(my_url)
        all_articles = page.findAll("div", "span6")
        # Slice to only 10 articles
        articles_slice = slice(0, 10)
        latest_articles = all_articles[articles_slice]

        for article in latest_articles:
            Article(
                title=article.h3.text.strip(),
                post_time_stamp=article.find("span", "time").text,
                post_description=article.p.text.strip(),
                thumbnail_url=article.img["src"],
                post_link=article.h3.a["href"]
            ).save()

        data = Article.objects.all()

        serializer = ArticleSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)
