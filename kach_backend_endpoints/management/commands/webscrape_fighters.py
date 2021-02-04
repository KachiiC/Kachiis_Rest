from django.core.management.base import BaseCommand
from urllib.request import urlopen
from bs4 import BeautifulSoup as Soup
from kach_backend_endpoints.backend_list.mma_divisions.mma_divisions_model import Division
from kach_backend_endpoints.backend_list.mma_fighters.mma_fighter_model import Fighter

my_url = "https://www.ufc.com/rankings"


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Delete all divisions and Fighters
        Division.objects.all().delete()
        Fighter.objects.all().delete()

        # grabbing page
        u_client = urlopen(my_url)
        # adds content into variable
        ufc_rankings_page = urlopen(my_url).read()
        # close urlopen
        u_client.close()

        # html parsing
        page = Soup(ufc_rankings_page, "html.parser")

        # grabs each product
        rankings = page.findAll("table")[:-1]

        for rank in rankings:
            division_name = rank.h4.text.strip()

            if division_name != "Men's Pound-for-Pound Top Rank" \
                    and division_name != "Women's Pound-for-Pound Top Rank":

                division_champion = rank.h5.text.strip().split()
                division_rankings = rank.findAll("tr")

                Fighter(
                    first_name=division_champion[0],
                    last_name=division_champion[1],
                    is_champion=True,
                    weight_class=division_name
                ).save()

                for division_fighter in division_rankings:
                    information = division_fighter.findAll("td")
                    fighter_name = information[1].text.strip().split()

                    Fighter(
                        first_name=fighter_name[0],
                        last_name=fighter_name[1],
                        rank=information[0].text,
                        is_champion=False,
                        weight_class=division_name,
                    ).save()

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

                print(f"{division_name} repopped")

        # Adds fighters to divisions
        all_fighters = Fighter.objects.all()
        all_divisions = Division.objects.all()

        for division in all_divisions:
            for fighter in all_fighters:
                if fighter.weight_class == division.weight_class:
                    division.fighters.add(fighter)

        print("repop_complete")
