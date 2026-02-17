import requests
from random import sample


def get_pokemon(pokemon: str):
    return requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon.title()}')


def pokemon_details(pokeinfo: dict):
    """
    Takes json from the api and extracts only the parts we care about
    """
    pk_types = []
    for i in range(0, len(pokeinfo['types'])):
        pk_types.append(pokeinfo['types'][i]['type']['name'].title())

    moves = pokeinfo['moves']
    move_numbers = sample(range(0, len(moves) - 1), 5)
    # print(moves[0])
    five_moves = []
    for i in move_numbers:
        five_moves.append(moves[i]['move']['name'].title())
    
    print(f"{pokeinfo['name'].title()}")
    print(f"Pokedex ID: {pokeinfo['id']}")
    print(f"Height: {pokeinfo['height'] / 10}m")
    print(f"Weight: {pokeinfo['weight'] / 10}kg")
    print(f"Type/s: {', '.join(pk_types)}")
    print(f"Move/s: {', '.join(five_moves)}\n")


cont = True
print('Hello there, I am your digital Pokedex!')
while cont:
    print('What Pokemon have you found or type Y to quit: ')
    pokemon = input()
    if pokemon.lower()== 'y':
        exit()
    res = get_pokemon(pokemon)

    if res.status_code not in (200, 201, 202):
        print('Ooh- you’ve found a MissingNo! \nPlease check your spelling to find the relevant Pokemon.')
    else:
        pokemon_details(res.json())
    ans = input('Do you want to look up another Pokemon? \nY/N')
    if ans.lower() in ('n', 'no'):
        cont = False
        print("Exit message here")




#need loop statement