from django.shortcuts import render
from .models import Pokemon
from .serializers import serialize_pokemon
from django.http import JsonResponse


def pokemon_list(request):
    pokemons = Pokemon.objects.all()
    return JsonResponse(serialize_pokemon(pokemons), safe=False)


