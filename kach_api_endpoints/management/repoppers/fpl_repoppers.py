import json
from kach_api_endpoints.api_list.fpl_api.fpl_model import MatchDay, Player, Chip


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

        for chip in data[0]["chips"]:
            Chip(
                chip_owner=data[1]["player_first_name"],
                chip_name=chip["name"],
                chip_date=chip["time"],
                chip_matchday=chip["event"]
            ).save()

        Player(
            player_id=data[1]["id"],
            player_name=data[1]["player_first_name"],
            points_total=data[1]["summary_overall_points"],
            transfers_total=data[1]["last_deadline_total_transfers"],
            current_gameweek=data[1]["current_event"]
        ).save()

