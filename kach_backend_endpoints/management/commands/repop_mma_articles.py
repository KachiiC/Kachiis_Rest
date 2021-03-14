from django.core.management.base import BaseCommand
from kach_backend_endpoints.management.url_webscrapper import url_webscraper

my_url = "https://www.mmafighting.com/latest-news"


class Command(BaseCommand):
    def handle(self, *args, **options):
        print(my_url)