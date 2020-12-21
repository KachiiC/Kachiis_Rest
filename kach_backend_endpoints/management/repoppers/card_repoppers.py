import json
from kach_backend_endpoints.backend_list.cards_api.card_model import Card


def create_new_cards(data_location):
    with open(data_location, 'r') as json_file:
        data = json.load(json_file)

        for card in data:
            Card(
                code=card["code"],
                value=card["value"],
                image=f"https://deckofcardsapi.com/static/img/{card['code']}.png",
                suit=card["suit"]
            ).save()