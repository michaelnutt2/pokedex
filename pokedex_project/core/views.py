from django.shortcuts import render
from .models import Pokemon

# Create your views here.
def pokemon_list(request):
    # Fetch data
    pokemon = Pokemon.objects.all().order_by('pokedex_number')[:10]
    # SELECT * FROM pokemon WHERE hp > 100
    tanks = Pokemon.objects.filter(hp__gt=100)

    # Select * FROM pokemon WHERE name LIKE '%izard%'
    izards = Pokemon.objects.filter(name__icontains='izard')

    context = {
        'pokemon_list': pokemon,
        'tanks': tanks,
        'izards': izards
    }

    return render(request, 'core/pokemon_list.html', context)

def pokemon_locations(request):
    # Fetch data
    pokemon = Pokemon.objects.all().order_by('pokedex_number')[:10]

    context = {
        'pokemon_list': pokemon,
    }

    return render(request, 'core/locations.html', context)

def python_logic(request):
    # Fetch data
    pokemon = Pokemon.objects.all()

    if pokemon.count() > 1000:
        message = "Warning: That's a lot of Pokemon!"
    else:
        message = "Whered did all the Pokemon go?"

    context = {
        'pokemon_list': pokemon[:10],
        'message': message,
    }

    return render(request, 'core/python.html', context)