from django.core.management.base import BaseCommand
from kach_backend_endpoints.management.url_webscrapper import url_webscraper
from ..repoppers.mma_p4p_repopper import create_mma_p4p

my_url = "https://www.ufc.com/rankings"


class Command(BaseCommand):
    def handle(self, *args, **options):
        # grabbing page
        page = url_webscraper(my_url)
        # grabs each division
        rankings = page.findAll("table")[:-1]

        print("Adding fighters to p4p_list...")
        pound_for_pound_tables = [0, 9]

        for division in pound_for_pound_tables:
            create_mma_p4p(rankings[division])
        print("p4p division added!")
