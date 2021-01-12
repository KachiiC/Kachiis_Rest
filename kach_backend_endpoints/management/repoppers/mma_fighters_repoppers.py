import json
from kach_backend_endpoints.backend_list.mma_fighters.mma_fighter_model import Fighter


def create_mma_fighters(data_location):
    with open(data_location, 'r') as json_file:
        data = json.load(json_file)

        for fighter in data:
            Fighter(
                first_name=fighter["first_name"],
                last_name=fighter["last_name"],
                nickname=fighter["nickname"],
                status=fighter["status"],
                date_of_birth=fighter["date_of_birth"],
                promotion=fighter["promotion"],
                rank=fighter["rank"],
                height=fighter["height"],
                reach=fighter["reach"],
                weight_class=fighter["weight_class"],
                style=fighter["style"],
                notable_wins=fighter["notable_wins"],
                wins=fighter["wins"],
                losses=fighter["losses"],
                draws=fighter["draws"],
                no_contests=fighter["no_contests"],
                wins_via_knockout=fighter["wins_via_knockout"],
                wins_via_submission=fighter["wins_via_submission"],
                wins_via_decision=fighter["wins_via_decision"],
                losses_via_knockout=fighter["losses_via_knockout"],
                losses_via_submission=fighter["losses_via_submission"],
                losses_via_decision=fighter["losses_via_decision"]
            ).save()
