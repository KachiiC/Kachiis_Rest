from django.urls import path
from .backend_list.hsk_api.hsk_view import hsk_words_list, hsk_single_word, all_hsk_levels, single_hsk_level

urlpatterns = [
    # HSK
    path("hsk_words/", hsk_words_list, name="hsk_words"),
    path("hsk_words/<str:chinese_characters>", hsk_single_word, name="hsk_single_word"),
    path("hsk_level/", all_hsk_levels, name="all_hsk_levels"),
    path("hsk_level/<int:level>", single_hsk_level, name="hsk_level")
]
