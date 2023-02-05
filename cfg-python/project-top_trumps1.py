import random
import requests

# get player ID and stats
player_id = random.randint(1,151)

url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(player_id)

response = requests.get(url)
pokemon = response.json()

player_pokemon = {
        "name": pokemon["name"],
        "id": player_id,
        "height": pokemon["height"],
        "weight": pokemon["weight"]
        }


# get opponent ID and stats
opponent_id = random.randint(1, 151)

url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(opponent_id)

response = requests.get(url)
pokemon = response.json()

opponent_pokemon = {
        "name": pokemon["name"],
        "id": opponent_id,
        "height": pokemon["height"],
        "weight": pokemon["weight"]
        }

# print out results of dictionaries
print(f'Your pokemon: {player_pokemon}')

stat_choice = input('Which stat would you like to use? ')
opponent_stat = opponent_pokemon[stat_choice]
opponent_name = opponent_pokemon["name"]

def comparison(x,y):
    if x < y:
        print('You win!')
    elif x > y:
        print('You lose!')
    else: print('Draw!')

if stat_choice in ['id', 'height', 'weight']:
    print(f'Opponent {opponent_name} {stat_choice}: {opponent_stat}')
    comparison(opponent_stat, player_pokemon[f'{stat_choice}'])
else: print('invalid choice')