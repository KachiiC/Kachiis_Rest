from kach_backend_endpoints.backend_list.mma_backend.mma_divisions.mma_divisions_model import Division
from kach_backend_endpoints.backend_list.mma_backend.mma_fighters.mma_fighter_model import Fighter
from .mma_fighter_repoppers import create_mma_fighter

excluded_fighter = "Jon Jones"


def create_mma_p4p(division):
    def get_fighter(first_name, last_name):
        find_fighter = Fighter.objects.get(
            first_name=first_name,
            last_name=last_name
        )

        return find_fighter

    p4p_title = division.h4.text.strip()

    ranked_first = division.h5.text.strip().split()

    p4p_division = Division.objects.get(weight_class=p4p_title)

    p4p_king = Fighter.objects.get(first_name=ranked_first[0], last_name=ranked_first[1])

    p4p_king.p4p_ranking = 1
    p4p_king.save()

    p4p_division.fighters.add(p4p_king)

    p4p_fighters = division.findAll("td", "views-field views-field-title")
    p4p_ranks = division.findAll("td", "views-field views-field-weight-class-rank")

    for fighter in p4p_fighters:
        p4p_fighter_rank = p4p_ranks[p4p_fighters.index(fighter)].text.strip()
        p4p_ranked_fighter = fighter.text.strip()
        p4p_fighter_name = p4p_ranked_fighter.split()
        p4p_first_name = p4p_fighter_name[0]
        p4p_last_name = p4p_fighter_name[1]

        if p4p_ranked_fighter == excluded_fighter:
            division_rank = "Not ranked"

            create_mma_fighter(p4p_fighter_name, division_rank, "Light Heavyweight")

            selected_fighter = get_fighter(p4p_first_name, p4p_last_name)

        else:
            if len(p4p_fighter_name) > 2:
                selected_fighter = get_fighter(p4p_first_name, ' '.join(p4p_fighter_name[1:]))

            else:
                selected_fighter = get_fighter(p4p_first_name, p4p_last_name)

        selected_fighter.p4p_ranking = p4p_fighter_rank
        selected_fighter.save()

        p4p_division.fighters.add(selected_fighter)
