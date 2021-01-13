from django.core.management.base import BaseCommand
from kach_backend_endpoints.backend_list.mma_fighters.mma_fighter_model import Fighter
from kach_backend_endpoints.backend_list.mma_fights.mma_fights_model import Fight


class Command(BaseCommand):
    def handle(self, *args, **options):

        all_fighters = Fighter.objects.all()
        all_fights = Fight.objects.all()

        for fighter in all_fighters:
            full_name = fighter.first_name + " " + fighter.last_name

            for fight in all_fights:
                if fight.blue_corner == full_name or Fight.red_corner == full_name and fight.notable_win == True:
                    fighter.notable_wins.add(fight)

        print("Done!")
