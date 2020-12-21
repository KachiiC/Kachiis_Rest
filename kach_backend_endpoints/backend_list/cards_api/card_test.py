from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from kach_backend_endpoints.backend_list.cards_api.card_model import Card
from kach_backend_endpoints.backend_list.cards_api.card_serializers import CardSerializer


class CardTest(APITestCase):
    cards_endpoint = reverse("cards_list")

    card_1 = Card(
        code="AS",
        value="Ace",
        image="https://deckofcardsapi.com/static/img/AS.png",
        suit="Spades"
    )

    card_2 = Card(
        code="QH",
        value="Queen",
        image="https://deckofcardsapi.com/static/img/QH.png",
        suit="Hearts"
    )

    expected_cards = [card_1, card_2]

    def setUp(self):
        for obj in self.expected_cards:
            obj.save()

    def test_get_all_cards(self):
        serializer = CardSerializer(self.expected_cards, many=True)

        response = self.client.get(self.cards_endpoint)
        assert response.status_code == status.HTTP_200_OK
        assert response.data == serializer.data
