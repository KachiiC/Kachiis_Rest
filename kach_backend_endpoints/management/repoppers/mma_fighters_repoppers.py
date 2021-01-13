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
                weight_class=fighter["weight"],
                style=fighter["style"],
                wins=fighter["W"],
                losses=fighter["L"],
                draws=fighter["D"],
                no_contests=fighter["NC"],
                wins_via_knockout=fighter["wins_via_ko"],
                wins_via_submission=fighter["wins_via_sub"],
                wins_via_decision=fighter["wins_via_dec"],
                losses_via_knockout=fighter["losses_via_ko"],
                losses_via_submission=fighter["losses_via_sub"],
                losses_via_decision=fighter["losses_via_dec"],
            ).save()
