from django.core.management.base import BaseCommand
from kach_backend_endpoints.management.url_webscrapper import url_webscraper
from kach_backend_endpoints.backend_list.mma_backend.mma_articles.mma_articles_model import Article

my_url = "https://www.mmaweekly.com/category/news"


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Delete all objects
        Article.objects.all().delete()

        # Grabs Articles
        page = url_webscraper(my_url)
        all_articles = page.findAll("div", "span6")
        # Slice to only 10 articles
        articles_slice = slice(0, 10)
        latest_articles = all_articles[articles_slice]

        for article in latest_articles:
            Article(
                title=article.h3.text.strip(),
                thumbnail_url=article.img["src"],
                post_time_stamp=article.find("span", "time").text,
                post_description=article.p.text.strip()
            ).save()

        print("article repop complete!")