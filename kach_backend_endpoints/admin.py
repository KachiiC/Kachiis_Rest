from django.contrib import admin
from .backend_list.hsk_api.hsk_model import Word, HSKLevel
from .backend_list.cards_api.card_model import Card
from .backend_list.mma_dictionary.mma_dictionary_model import Dictionary
from .backend_list.mma_techniques.mma_techniques_model import Technique
from .backend_list.mma_fighters.mma_fighter_model import Fighter

admin.site.register(Word)  # HSK Word
admin.site.register(HSKLevel)  # HSK Level
admin.site.register(Card)  # Card
admin.site.register(Dictionary)  # Dictionary
admin.site.register(Technique)  # Technique
admin.site.register(Fighter)  # Fighter
