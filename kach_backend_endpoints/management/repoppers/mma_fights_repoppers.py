import json
from kach_backend_endpoints.backend_list.mma_fights.mma_fights_model import Fight


def create_mma_fights(data_location):
    with open(data_location, 'r') as json_file:
        data = json.load(json_file)

        for fight in data:
            Fight(
                red_corner=fight["red_corner"],
                blue_corner=fight["blue_corner"],
                winner=fight["winner"],
                method_of_victory=fight["method_of_victory"],
                round=fight["round"],
                draw=fight["draw"],
                weight_class=fight["weight_class"],
                title_fight=fight["title_fight"],
                video=fight["video"],
                event=fight["event"],
                date=fight["date"],
                notable_win=fight["notable_win"]
            ).save()
