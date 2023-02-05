import random
import requests

# get player ID and stats
player_id = random.randint(1,151)

url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(player_id)

response = requests.get(url)
pokemon = response.json()

player_pokemon = {
        "name": pokemon["name"], 
        "number": player_id, 
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
        "number": opponent_id, 
        "height": pokemon["height"],
	    "weight": pokemon["weight"]
        }

# print out results of dictionaries
print(player_pokemon, "\n", opponent_pokemon)

# ask which stat to compare
compare = input("Which stat would you like to compare? number/height/weight ")

# compare stats
if player_pokemon[compare] > opponent_pokemon[compare]:
    print("You chose {} with a {} of {}. Your opponent chose {} with a {} of {}. You win.".format(player_pokemon["name"],compare,player_pokemon[compare],opponent_pokemon["name"],compare,opponent_pokemon[compare]))

elif player_pokemon[compare] < opponent_pokemon[compare]:
    print("You chose {} with a {} of {}. Your opponent chose {} with a {} of {}. You lose.".format(player_pokemon["name"],compare,player_pokemon[compare],opponent_pokemon["name"],compare,opponent_pokemon[compare]))

else:
    print("You chose {} with a {} of {}. Your opponent chose {} with a {} of {}. You draw.".format(player_pokemon["name"],compare,player_pokemon[compare],opponent_pokemon["name"],compare,opponent_pokemon[compare]))