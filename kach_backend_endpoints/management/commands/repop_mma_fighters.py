from django.core.management.base import BaseCommand
from kach_backend_endpoints.management.url_webscrapper import url_webscraper
from kach_backend_endpoints.backend_list.mma_divisions.mma_divisions_model import Division
from kach_backend_endpoints.backend_list.mma_fighters.mma_fighter_model import Fighter
from kach_backend_endpoints.management.repoppers.mma_fighter_repoppers import create_mma_fighter

my_url = "https://www.ufc.com/rankings"


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Delete all divisions and Fighters
        Division.objects.all().delete()
        Fighter.objects.all().delete()

        # grabbing page
        page = url_webscraper(my_url)
        # grabs each division
        rankings = page.findAll("table")[:-1]

        for rank in rankings:
            division_name = rank.h4.text.strip()

            if division_name.split()[0] == "Women's":
                division_gender = "Women"
            else:
                division_gender = "Men"

            if division_name != "Men's Pound-for-Pound Top Rank" \
                    and division_name != "Women's Pound-for-Pound Top Rank":

                division_champion = rank.h5.text.strip().split()
                create_mma_fighter(division_champion, "champion", division_name)

                division_rankings = rank.findAll("tr")

                for division_fighter in division_rankings:
                    fighter_info = division_fighter.findAll("td")

                    fighter_name = fighter_info[1].text.strip().split()

                    fighter_rank = fighter_info[0].text

                    create_mma_fighter(fighter_name, fighter_rank, division_name)

            Division(
                weight_class=division_name,
                gender=division_gender,
                pound_for_pound=False
            ).save()

            print(f"{division_name} added...")

        else:
            Division(
                weight_class=division_name,
                gender=division_gender,
                pound_for_pound=True
            ).save()

        # Adds fighters to divisions
        all_fighters = Fighter.objects.all()
        all_divisions = Division.objects.all()

        print("Adding fighters to correct divisions...")

        for division in all_divisions:
            for fighter in all_fighters:
                if fighter.weight_class == division.weight_class:
                    division.fighters.add(fighter)

        print("All divisions added...")

        print("Repop Complete!")
