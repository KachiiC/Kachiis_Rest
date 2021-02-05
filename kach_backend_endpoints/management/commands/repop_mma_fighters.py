import math

from django.core.management.base import BaseCommand
from urllib.request import urlopen
from bs4 import BeautifulSoup as Soup
from kach_backend_endpoints.backend_list.mma_divisions.mma_divisions_model import Division
from kach_backend_endpoints.backend_list.mma_fighters.mma_fighter_model import Fighter

my_url = "https://www.ufc.com/rankings"

excluded_fighter = "Kai Kara France"


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Delete all divisions and Fighters
        Division.objects.all().delete()
        print("Divisions deleted...")
        Fighter.objects.all().delete()
        print("Fighters deleted...")

        # grabbing page
        u_client = urlopen(my_url)
        # adds content into variable
        ufc_rankings_page = urlopen(my_url).read()
        # close urlopen
        u_client.close()
        print("URL read..")

        # html parsing
        page = Soup(ufc_rankings_page, "html.parser")
        print("opened page")

        # grabs each product
        rankings = page.findAll("table")[:-1]
        print("table found...")

        for rank in rankings:
            division_name = rank.h4.text.strip()
            print("division name found...")

            if division_name.split()[0] == "Women's":
                division_gender = "Women"
            else:
                division_gender = "Men"

            if division_name != "Men's Pound-for-Pound Top Rank" \
                    and division_name != "Women's Pound-for-Pound Top Rank":

                print("division name")

                division_champion = rank.h5.text.strip().split()
                division_rankings = rank.findAll("tr")

                champion_url = f"https://www.ufc.com/athlete/{'-'.join(division_champion)}"

                ufc_champ = urlopen(champion_url).read()

                champ_page = Soup(ufc_champ, "html.parser")

                if len(division_champion) > 2:
                    champ_first_name = division_champion[0]
                    champ_last_name = " ".join([division_champion[1], division_champion[2]])
                else:
                    champ_first_name = division_champion[0]
                    champ_last_name = division_champion[1]

                champ_image_link = champ_page.find("div", {"c-bio__image"}).img["src"]
                print("division champion")

                # MMA Record
                mma_record = champ_page.find(
                    "div", "c-hero__headline-suffix tz-change-inner"
                ).text.split()[-2].split("-")

                champ_wins = int(mma_record[0])
                champ_losses = int(mma_record[1])
                champ_draws = int(mma_record[2])

                # MMA Wins
                champ_wins_method = champ_page.findAll(
                    "div", "c-stats-group-3col__item"
                )[2].find(
                    "div", "c-stat-3bar__legend"
                ).findAll("div", "c-stat-3bar__value")

                champ_ko_wins = int(champ_wins_method[0].text.split()[0])
                champ_decision_wins = int(champ_wins_method[1].text.split()[0])
                champ_sub_wins = int(champ_wins_method[2].text.split()[0])

                # STATS
                # champ_accuracy = champ_page.findAll("text", {"e-chart-circle__percent"})
                # champ_striking_accuracy = champ_accuracy[0].text
                # champ_grappling_accuracy = champ_accuracy[1].text

                # AGE
                champ_age = int(champ_page.find("div", "field--name-age").text)

                champ_info = champ_page.findAll("div", "c-bio__row--3col")

                champ_reach = float(champ_info[1].findAll("div", "c-bio__text")[1].text)

                champ_height_inches = float(champ_info[0].findAll("div", "c-bio__text")[1].text)

                champ_display_height = str(math.floor((champ_height_inches / 12))) + "ft" + str(
                    round(champ_height_inches % 12))

                print("data correctly pulled...")

                Fighter(
                    first_name=champ_first_name,
                    last_name=champ_last_name,
                    is_champion=True,
                    weight_class=division_name,
                    age=champ_age,
                    height=champ_display_height,
                    reach=champ_reach,
                    wins=champ_wins,
                    losses=champ_losses,
                    draws=champ_draws,
                    wins_via_ko=champ_ko_wins,
                    wins_via_sub=champ_sub_wins,
                    wins_via_dec=champ_decision_wins,
                    fighter_image=champ_image_link,
                ).save()

                print(f"{' '.join(division_champion)} added")

                for division_fighter in division_rankings:
                    information = division_fighter.findAll("td")
                    site_fighter_name_letters = list(information[1].text.strip())

                    for letter in site_fighter_name_letters:
                        if letter == "ñ":
                            site_fighter_name_letters[site_fighter_name_letters.index(letter)] = "n"

                    fighter_name = ("".join(site_fighter_name_letters)).split()

                    if " ".join(fighter_name) != excluded_fighter:

                        if len(fighter_name) > 2:
                            fighter_first_name = fighter_name[0]
                            fighter_last_name = " ".join([fighter_name[1], fighter_name[2]])
                        else:
                            fighter_first_name = fighter_name[0]
                            fighter_last_name = fighter_name[1]

                        fighter_url = f"https://www.ufc.com/athlete/{'-'.join(fighter_name)}"

                        ufc_single_fighter = urlopen(fighter_url).read()

                        fighter_page = Soup(ufc_single_fighter, "html.parser")

                        fighter_image_link = fighter_page.find("div", {"c-bio__image"}).img["src"]

                        # MMA Record
                        fighter_record = fighter_page.find(
                            "div", {"c-hero__headline-suffix tz-change-inner"}
                        ).text.split()[-2].split("-")

                        fighter_wins = fighter_record[0]
                        fighter_losses = fighter_record[1]
                        fighter_draws = fighter_record[2]

                        # MMA Wins
                        fighter_wins_method = fighter_page.findAll(
                            "div", "c-stats-group-3col__item"
                        )[2].find(
                            "div", "c-stat-3bar__legend"
                        ).findAll("div", "c-stat-3bar__value")

                        fighter_ko_wins = fighter_wins_method[0].text.split()[0]
                        fighter_decision_wins = fighter_wins_method[1].text.split()[0]
                        fighter_sub_wins = fighter_wins_method[2].text.split()[0]

                        # STATS
                        # fighter_accuracy = fighter_page.findAll("text", {"e-chart-circle__percent"})
                        # fighter_striking_accuracy = fighter_accuracy[0].text
                        # fighter_grappling_accuracy = fighter_accuracy[1].text

                        # AGE
                        fighter_age = int(fighter_page.find("div", "field--name-age").text)

                        fighter_info = fighter_page.findAll("div", "c-bio__row--3col")

                        fighter_reach = float(fighter_info[1].findAll("div", "c-bio__text")[1].text)

                        fighter_height_inches = float(fighter_info[0].findAll("div", "c-bio__text")[1].text)

                        fighter_display_height = str(math.floor((fighter_height_inches / 12))) + "ft" + str(
                            round(fighter_height_inches % 12))

                        Fighter(
                            first_name=fighter_first_name,
                            last_name=fighter_last_name,
                            rank=information[0].text,
                            is_champion=False,
                            weight_class=division_name,
                            age=fighter_age,
                            height=fighter_display_height,
                            reach=fighter_reach,
                            wins=fighter_wins,
                            losses=fighter_losses,
                            draws=fighter_draws,
                            wins_via_ko=fighter_ko_wins,
                            wins_via_sub=fighter_sub_wins,
                            wins_via_dec=fighter_decision_wins,
                            fighter_image=fighter_image_link
                        ).save()

                        print(f"{' '.join(fighter_name)} saved")

                Division(
                    weight_class=division_name,
                    gender=division_gender,
                    pound_for_pound=False
                ).save()

                print(f"{division_name} repopped...")

            else:
                Division(
                    weight_class=division_name,
                    gender=division_gender,
                    pound_for_pound=True
                ).save()

        # Adds fighters to divisions
        all_fighters = Fighter.objects.all()
        all_divisions = Division.objects.all()

        print("adding fighters to correct divisions...")
        for division in all_divisions:
            for fighter in all_fighters:
                if fighter.weight_class == division.weight_class:
                    division.fighters.add(fighter)
        print(f"${division} added...")

        print("repop_complete!")
