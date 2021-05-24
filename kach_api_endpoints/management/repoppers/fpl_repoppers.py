import functools
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
            if chip["name"] == "3xc":
                output = "Triple Captain"
            elif chip["name"] == "bboost":
                output = "Bench Boost"
            elif chip["name"] == "freehit":
                output = "Free Hit"
            elif chip["name"] == "wildcard":
                output = "Wild Card"

            Chip(
                chip_owner=data[1]["player_first_name"],
                chip_name=output,
                chip_date=chip["time"],
                chip_matchday=chip["event"]
            ).save()

        transfer_points = []

        for single_data in data[0]["current"]:
            transfer_points.append(single_data["event_transfers_cost"])

        Player(
            player_id=data[1]["id"],
            player_name=data[1]["player_first_name"],
            team_name=data[1]["name"],
            current_gameweek=data[1]["current_event"],
            last_gameweek_points=data[1]["summary_event_points"],
            points_total=data[1]["summary_overall_points"],
            transfers_total=data[1]["last_deadline_total_transfers"],
            team_value=data[1]['last_deadline_value'],
            points_on_transfers=functools.reduce(lambda a, b: a + b, transfer_points),
        ).save()
