from django.contrib import admin
from .backend_list.hsk_api.hsk_model import Word, HSKLevel
from .backend_list.cards_api.card_model import Card

admin.site.register(Word)  # HSK Word
admin.site.register(HSKLevel)  # HSK Level
admin.site.register(Card)  # Card
