from django.shortcuts import render
from .models import Pokemon

# Create your views here.
def pokemon_list(request):
    # Fetch data
    pokemon = Pokemon.objects.all().order_by('pokedex_number')[:50]

    context = {
        'pokemon_list': pokemon
    }

    return render(request, 'core/pokemon_list.html', context)