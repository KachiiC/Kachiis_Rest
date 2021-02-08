import math
from kach_backend_endpoints.management.url_webscrapper import url_webscraper
from kach_backend_endpoints.backend_list.mma_fighters.mma_fighter_model import Fighter

excluded_fighter = "Kai Kara France"


def create_mma_fighter(fighter, rank, division):
    fighter_name_letters = list(" ".join(fighter))

    for letter in fighter_name_letters:
        if letter == "ñ":
            fighter_name_letters[fighter_name_letters.index(letter)] = "n"

    fighter_name = "".join(fighter_name_letters).split()

    if " ".join(fighter_name) != excluded_fighter:
        fighter_url = f"https://www.ufc.com/athlete/{'-'.join(fighter_name)}"
        fighter_page = url_webscraper(fighter_url)

        # Code Set Ups

        # Fighter record set up
        fighter_record = fighter_page.find(
            "div", {"c-hero__headline-suffix tz-change-inner"}
        ).text.split()[-2].split("-")
        # Fighter win types set up
        fighter_wins_method = fighter_page.findAll(
            "div", "c-stats-group-3col__item"
        )[2].find(
            "div", "c-stat-3bar__legend"
        ).findAll("div", "c-stat-3bar__value")
        # Fighter info set up
        fighter_info = fighter_page.findAll("div", "c-bio__row--3col")
        # Fighter height set up
        fighter_height_inches = float(fighter_info[0].findAll("div", "c-bio__text")[1].text)

        # Saved Info
        if len(fighter_name) > 2:
            fighter_first_name = fighter_name[0]
            fighter_last_name = " ".join([fighter_name[1], fighter_name[2]])
        else:
            fighter_first_name = fighter_name[0]
            fighter_last_name = fighter_name[1]

        if rank == "champion":
            fighter_rank = None
            is_champion = True
        else:
            fighter_rank = rank
            is_champion = False

        # Fighter Image
        fighter_image_link = fighter_page.find("div", {"c-bio__image"}).img["src"]
        # Wins
        fighter_wins = fighter_record[0]
        # Losses
        fighter_losses = fighter_record[1]
        # Draws
        fighter_draws = fighter_record[2]
        # Knockouts
        fighter_ko_wins = fighter_wins_method[0].text.split()[0]
        # Decisions
        fighter_decision_wins = fighter_wins_method[1].text.split()[0]
        # Subs
        fighter_sub_wins = fighter_wins_method[2].text.split()[0]
        # AGE
        fighter_age = int(fighter_page.find("div", "field--name-age").text)
        # Reach
        fighter_reach = float(fighter_info[1].findAll("div", "c-bio__text")[1].text)
        # Height
        fighter_display_height = str(math.floor((fighter_height_inches / 12))) + "ft" + str(
            round(fighter_height_inches % 12))

        Fighter(
            first_name=fighter_first_name,
            last_name=fighter_last_name,
            is_champion=is_champion,
            rank=fighter_rank,
            weight_class=division,
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
