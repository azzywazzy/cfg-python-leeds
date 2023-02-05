import random
import requests

# get 5 random pokemon IDs and store in a list
pokemon_ids = []
for x in range(5):
    random_id = random.randint(1,151)
    pokemon_ids.append(random_id)

    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(random_id)

    response = requests.get(url)
    pokemon = response.json()

    pokemon_name = pokemon["name"]
    print(pokemon_name)

# get user to choose which pokemon they want to battle with
pokemon_choice = input("\nChoose which Pokemon you'd like to battle with, from the list above: ")
print("\n{}, I CHOOSE YOU!\n".format(pokemon_choice))

# get opponent ID and stats
opponent_id = random.randint(1, 151)

# pick the moves to choose from
move_name = random.sample(pokemon["moves"],5)
for x in move_name:
    move_names = x["move"]["name"]
    print(move_names)

# get user to choose which move they want to battle with
move_choice = input("\nChoose which move you'd like to use: ")
print("\nYou chose {} and will battle with {}!\n".format(pokemon_choice, move_choice))

player_url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_choice)

moves = pokemon["moves"]

# for move in moves:
#     print("This pokemon has move {}".format(move["move"]["name"]))  