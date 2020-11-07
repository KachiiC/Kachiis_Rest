import json
from kach_api_endpoints.api_list.fpl_api.fpl_model import MatchDay, Player


def create_fpl_data(data_location):
    with open(data_location, 'r') as json_file:
        data = json.load(json_file)

        for match in data[0]["current"]:
            MatchDay(
                player_id=data[1]["id"],
                gameweek=match["event"],
                game_week_points=match["points"],
                points_total=match["total_points"],
                team_value=match["value"],
                game_week_transfers=match["event_transfers"],
                game_week_transfers_cost=match["event_transfers_cost"],
                bench_points=match["points_on_bench"]
            ).save()

        Player(
            player_id=data[1]["id"],
            player_name=data[1]["player_first_name"]
        ).save()
