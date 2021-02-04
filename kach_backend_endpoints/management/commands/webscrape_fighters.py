from django.core.management.base import BaseCommand
from urllib.request import urlopen
from bs4 import BeautifulSoup as Soup
from kach_backend_endpoints.backend_list.mma_divisions.mma_divisions_model import Division

my_url = "https://www.ufc.com/rankings"


class Command(BaseCommand):
    def handle(self, *args, **options):
        # grabbing page
        u_client = urlopen(my_url)
        # adds content into variable
        ufc_rankings_page = urlopen(my_url).read()
        # close urlopen
        u_client.close()

        # html parsing
        page = Soup(ufc_rankings_page, "html.parser")

        # grabs each product
        rankings = page.findAll("table")

        for rank in rankings:
            division_name = rank.h4.text.strip()

            if division_name.split()[0] == "Women's":
                division_gender = "Women"
            else:
                division_gender = "Men"

            if len(division_name.split()) == 4:
                is_pound_for_pound = True
            else:
                is_pound_for_pound = False

            Division(
                weight_class=division_name,
                gender=division_gender,
                pound_for_pound=is_pound_for_pound
            ).save()

        print("repop_complete")
