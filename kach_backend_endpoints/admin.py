from django.contrib import admin
from .backend_list.hsk_api.hsk_model import Word, HSKLevel
from .backend_list.cards_api.card_model import Card
from kach_backend_endpoints.backend_list.mma_backend.mma_dictionary.mma_dictionary_model import Dictionary
from kach_backend_endpoints.backend_list.mma_backend.mma_techniques.mma_techniques_model import Technique
from kach_backend_endpoints.backend_list.mma_backend.mma_fighters.mma_fighter_model import Fighter
from kach_backend_endpoints.backend_list.mma_backend.mma_fights.mma_fights_model import Fight
from kach_backend_endpoints.backend_list.mma_backend.mma_divisions.mma_divisions_model import Division
from kach_backend_endpoints.backend_list.mma_backend.mma_articles.mma_articles_model import Article

admin.site.register(Word)  # HSK Word
admin.site.register(HSKLevel)  # HSK Level
admin.site.register(Card)  # Card
# MMA Backend
admin.site.register(Dictionary)  # Dictionary
admin.site.register(Technique)  # Technique
admin.site.register(Fighter)  # Fighter
admin.site.register(Fight)  # Fight
admin.site.register(Division)  # Division
admin.site.register(Article)  # Article
