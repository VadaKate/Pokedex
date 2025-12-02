import requests
from random import sample

print('Hello there, I am your digital Pokedex!')
pokemon = ('PIKACHU')#input('What Pokemon are you looking for?')
pokemon = pokemon.title()
res = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
res.raise_for_status()
print(res.status_code)
# print(res.text)
pk_data = res.json()
pokedex_id = pk_data['id']
height = pk_data['height']
weight = pk_data['weight']
# print(pk_data['moves'])
moves = pk_data['moves']
# print(len(moves))
move_numbers = sample(range(0, len(moves)-1), 5)
# print(moves[0])
five_moves = []
for i in move_numbers:
    five_moves.append(moves[i]['move']['name'].title())
print(', '.join(five_moves))
# print(pk_data['types'])
pk_types = []
for i in range(0,len(pk_data['types'])):
    pk_types.append(pk_data['types'][i]['type']['name'].title())
print(', '.join(pk_types))