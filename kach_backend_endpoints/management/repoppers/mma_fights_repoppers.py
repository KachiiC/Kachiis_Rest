import json
from kach_backend_endpoints.backend_list.mma_fights.mma_fights_model import Fight
from kach_backend_endpoints.backend_list.mma_fighters.mma_fighter_model import Fighter


def create_mma_fights(data_location):
    with open(data_location, 'r') as json_file:
        data = json.load(json_file)

        for fight in data:
            red = fight["red_corner"].split(" ")
            red_fighter = Fighter.objects.get(first_name=red[0], last_name=red[1])

            blue = fight["blue_corner"].split(" ")
            blue_fighter = Fighter.objects.get(first_name=blue[0], last_name=blue[1])

            Fight(
                red_corner=red_fighter,
                blue_corner=blue_fighter,
                winner=fight["winner"],
                method_of_victory=fight["method_of_victory"],
                round=fight["round"],
                draw=fight["draw"],
                weight_class=fight["weight_class"],
                title_fight=fight["title_fight"],
                video=fight["video"],
                event=fight["event"],
                date=fight["date"],
            ).save()
