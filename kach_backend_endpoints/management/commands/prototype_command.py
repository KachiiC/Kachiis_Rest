from django.core.management.base import BaseCommand
from kach_backend_endpoints.management.url_webscrapper import url_webscraper
from kach_backend_endpoints.backend_list.mma_divisions.mma_divisions_model import Division
from kach_backend_endpoints.backend_list.mma_fighters.mma_fighter_model import Fighter

my_url = "https://www.ufc.com/rankings"


class Command(BaseCommand):
    def handle(self, *args, **options):
        Division.objects.all().delete()
        Fighter.objects.all().delete()

