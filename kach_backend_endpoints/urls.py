from django.urls import path
from .backend_list.hsk_api.hsk_view import hsk_words_list, hsk_single_word, all_hsk_levels, single_hsk_level
from .backend_list.cards_api.card_view import cards_list
from kach_backend_endpoints.backend_list.mma_backend.mma_dictionary.mma_dictionary_view import mma_dictionary_list
from kach_backend_endpoints.backend_list.mma_backend.mma_techniques.mma_techniques_view import mma_techniques_list
from kach_backend_endpoints.backend_list.mma_backend.mma_fighters.mma_fighter_view import mma_fighter_list, FeaturedFighterApiView
from kach_backend_endpoints.backend_list.mma_backend.mma_fights.mma_fights_view import mma_fights_list
from kach_backend_endpoints.backend_list.mma_backend.mma_divisions.mma_divisions_view import mma_divisions_list

urlpatterns = [
    # HSK
    path("hsk_words/", hsk_words_list, name="hsk_words"),
    path("hsk_words/<str:chinese_characters>", hsk_single_word, name="hsk_single_word"),
    path("hsk_level/", all_hsk_levels, name="all_hsk_levels"),
    path("hsk_level/<int:level>", single_hsk_level, name="hsk_level"),
    # Cards
    path("cards_list/", cards_list, name="cards_list"),
    # MMA Dictionary List
    path("mma_dictionary_list/", mma_dictionary_list, name="mma_dictionary_list"),
    # MMA Technique List
    path('mma_techniques_list/', mma_techniques_list, name="mma_techniques_list"),
    # MMA Fighter List
    path('mma_fighters_list/', mma_fighter_list, name="mma_fighter_list"),
    path("mma_featured_fighter/", FeaturedFighterApiView.as_view(), name="mma_featured_fighter"),
    # MMA Fights List
    path('mma_fights_list/', mma_fights_list, name="mma_fights_list"),
    # MMA Divisions
    path('mma_divisions_list/', mma_divisions_list, name="mma_divisions_list"),
]
