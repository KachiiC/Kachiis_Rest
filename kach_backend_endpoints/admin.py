from django.contrib import admin
from .backend_list.hsk_api.hsk_model import Word, HSKLevel

admin.site.register(Word)  # HSK Word
admin.site.register(HSKLevel)  # HSK Level