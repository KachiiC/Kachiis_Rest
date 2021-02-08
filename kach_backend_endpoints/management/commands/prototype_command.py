from django.core.management.base import BaseCommand
from kach_backend_endpoints.management.url_webscrapper import url_webscraper
from kach_backend_endpoints.backend_list.mma_divisions.mma_divisions_model import Division
from kach_backend_endpoints.backend_list.mma_fighters.mma_fighter_model import Fighter

my_url = "https://www.ufc.com/rankings"


class Command(BaseCommand):
    def handle(self, *args, **options):
        # grabbing page
        page = url_webscraper(my_url)
        # grabs each division
        rankings = page.findAll("table")[:-1]

        # Mens Pound for Pound Set Up
        mens_pfp_title = rankings[0].h4.text.strip()
        ranked_first = rankings[0].h5.text.strip().split()


        # Womens Pound for Pound Set Up

        womens_pfp_title = rankings[9].h4.text.strip()

        mens_pfp = Division.objects.get(weight_class=mens_pfp_title)
        ranked_first_fighter = Fighter.objects.get(first_name=ranked_first[0], last_name=ranked_first[1])
        mens_pfp.fighters.add(ranked_first_fighter)

        print("complete!")
