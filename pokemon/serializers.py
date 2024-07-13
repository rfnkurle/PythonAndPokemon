from .models import Pokemon
from typing import Iterable, List, Dict, Any


def serialize_pokemon(pokemons: Iterable[Pokemon]) -> List[Dict[str, Any]]:
    data = []
    for pokemon in pokemons:
        data.append({
            'name': pokemon.name,
            'power': pokemon.power,
            'photo_url': pokemon.photo_url,
        })
    return data
