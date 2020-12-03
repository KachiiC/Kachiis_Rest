from django.urls import path
from .backend_list.hsk_api import hsk_view

urlpatterns = [
    # HSK
    path("hsk_words/", hsk_view.hsk_words_list, name="hsk_words"),
    path("hsk_words/<str:chinese_characters>", hsk_view.hsk_single_word, name="hsk_single_word"),
    path("hsk_level/", hsk_view.all_hsk_levels, name="all_hsk_levels"),
    path("hsk_level/<int:level>", hsk_view.single_hsk_level, name="hsk_level")
]
