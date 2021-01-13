from django.core.management.base import BaseCommand
from kach_backend_endpoints.backend_list.mma_fighters.mma_fighter_model import Fighter
from kach_backend_endpoints.backend_list.mma_fights.mma_fights_model import Fight


class Command(BaseCommand):
    def handle(self, *args, **options):
        myData = [
            {
                "first_name": "Anthony",
                "last_name": "Pettis",
            },
            {
                "first_name": "Benson",
                "last_name": "Henderson",
            },
            {
                "first_name": "Dan",
                "last_name": "Henderson",
            },

        ]

        fighter = Fighter.objects.get(first_name=myData[0]["first_name"], last_name=myData[0]["last_name"])

        print(fighter)
