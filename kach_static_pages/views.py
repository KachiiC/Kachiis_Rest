from django.shortcuts import render
from .models import DisplayCard

def home(request):
    context = {
        'display_cards': DisplayCard.objects.all()
    }
    return render(request, 'index.html', context)
