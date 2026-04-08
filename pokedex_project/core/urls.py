from django.urls import path
from . import views

# Inside the CORE folder

urlpatterns = [
    path('pokemon/', views.pokemon_list, name='pokemon_list'),
    path('locations/', views.pokemon_locations, name='pokemon_locations'),
    path('python/', views.python_logic, name='python_logic')
]