"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()

from pokemon.models import Pokemon
Pokemon.objects.create(name='Pikachu', power='poison', photo_url='https://assets.pokemon.com/assets/cms2/img/pokedex/full//006.png')
Pokemon.objects.create(name='Charizard',power='fire', photo_url='https://assets.pokemon.com/assets/cms2/img/pokedex/full//006.png')
Pokemon.objects.create(name='Bulbasaur', power='poison', photo_url='https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcT7i1N2B9yf9M47k-TsfBgcctSXSm7VbQFccuVrJ0ofT2KDWWrn')
Pokemon.objects.create(name='Charmander', power='sass', photo_url='https://assets.pokemon.com/assets/cms2/img/pokedex/full//004.png')
