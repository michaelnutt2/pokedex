from django.urls import path
from . import views

# Inside the CORE folder

urlpatterns = [
    path('pokemon/', views.pokemon_list, name='pokemon_list'),
]