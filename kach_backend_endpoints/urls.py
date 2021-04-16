from django.urls import path
from .backend_list.hsk_api.hsk_view import hsk_words_list, hsk_single_word, all_hsk_levels, single_hsk_level
from .backend_list.cards_api.card_view import cards_list
from .backend_list.mma_backend.mma_articles.mma_articles_cache_view import MMAArticlesView
from .backend_list.mma_backend.mma_dictionary.mma_dictionary_view import mma_dictionary_list
from .backend_list.mma_backend.mma_techniques.mma_techniques_view import mma_techniques_list
from .backend_list.mma_backend.mma_fighters.mma_fighter_view import mma_fighter_list, FeaturedFighterApiView
from .backend_list.mma_backend.mma_fights.mma_fights_view import mma_fights_list
from .backend_list.mma_backend.mma_divisions.mma_divisions_view import mma_divisions_list, mma_mens_p4p, mma_womens_p4p
from .backend_list.mma_backend.mma_store.mma_store_view import mma_store_list

urlpatterns = [
    # HSK
    path("hsk_words/", hsk_words_list, name="hsk_words"),
    path("hsk_words/<str:chinese_characters>", hsk_single_word, name="hsk_single_word"),
    path("hsk_level/", all_hsk_levels, name="all_hsk_levels"),
    path("hsk_level/<int:level>", single_hsk_level, name="hsk_level"),
    # Cards
    path("cards_list/", cards_list, name="cards_list"),
    # MMA Article List
    path("mma_articles_list", MMAArticlesView.as_view(), name="mma_articles_refresh"),
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
    path('mma_divisions_list/mma_mens_p4p/', mma_mens_p4p, name="mma_mens_p4p"),
    path('mma_divisions_list/mma_womens_p4p/', mma_womens_p4p, name="mma_womens_p4p"),
    # MMA Store
    path("mma_store_list/", mma_store_list, name="mma_store_list")
]
