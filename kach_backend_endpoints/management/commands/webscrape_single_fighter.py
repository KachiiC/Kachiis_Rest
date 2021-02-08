import math
from django.core.management.base import BaseCommand
from kach_backend_endpoints.management.url_webscrapper import url_webscraper
from kach_backend_endpoints.backend_list.mma_divisions.mma_divisions_model import Division
from kach_backend_endpoints.backend_list.mma_fighters.mma_fighter_model import Fighter
from ..repoppers.mma_fighter_repoppers import create_mma_fighter

my_url = "https://www.ufc.com/rankings"

excluded_fighter = "Kai Kara France"


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Delete all divisions and Fighters
        Division.objects.all().delete()
        Fighter.objects.all().delete()

        # grabbing page
        page = url_webscraper(my_url)

        # grabs each product
        rankings = page.findAll("table")[:-1]

        for rank in rankings:
            division_name = rank.h4.text.strip()

            if division_name != "Men's Pound-for-Pound Top Rank" \
                    and division_name != "Women's Pound-for-Pound Top Rank":
                division_champion = rank.h5.text.strip().split()

                create_mma_fighter(division_champion, "champion", division_name)

                print(f"{'-'.join(division_name)} added")
