import random
import requests

# get 5 random pokemon IDs and store in a list
print('Pokemon in your Pokedex:')
pokemon_ids = []
for x in range(5):
    random_id = random.randint(1,151)
    pokemon_ids.append(random_id)

    random_url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(random_id)
    random_response = requests.get(random_url)
    pokemon = random_response.json()
    pokemon_name = pokemon["name"]
    print(pokemon_name)

# get user to choose which pokemon they want to battle with
pokemon_choice = input("Please choose a pokemon for battle: ")
i_choose_you = f'\n{pokemon_choice}, I CHOOSE YOU!\n'
print(i_choose_you.upper())

# player pokemon stats
player_url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_choice}/'
player_response = requests.get(player_url)
chosen_pokemon = player_response.json()
hp = int(chosen_pokemon['stats'][0]['base_stat'])
print(f'{pokemon_choice.upper()} has hp: {hp}')

# opponent pokemon and stats
random_id = random.randint(1,151)
opponent_url = f'https://pokeapi.co/api/v2/pokemon/{random_id}/'
opponent_response = requests.get(opponent_url)
opponent_pokemon = opponent_response.json()
opponent_pokemon_name = opponent_pokemon['name']
opponent_hp = int(opponent_pokemon['stats'][0]['base_stat'])
print(f'Opponent chooses {opponent_pokemon_name.upper()} with hp: {opponent_hp}\n')

# player move with random choice of 5 moves
def player_move():
    def move_choices():
        print('Your pokemon\'s moves:')
        if len(pokemon['moves']) >= 5:
            moves = random.sample(pokemon['moves'], 5)
        else: moves = random.sample(pokemon['moves'], len(pokemon['moves']))
        for x in moves:
            move_names = x['move']['name']
            print(move_names)
    move_choices()
    move_choice = input(f'\nPlease choose a move: ')
    player_attack_command = f'\n{pokemon_choice}, {move_choice}!\n'
    print(player_attack_command.upper())

    # stats from user's move choice
    move_url = f'https://pokeapi.co/api/v2/move/{move_choice}/'
    move_response = requests.get(move_url)
    chosen_move = move_response.json()
    if chosen_move['power'] == None:
        power = 0
    else: power = int(chosen_move['power'])
    if opponent_hp - power >= 0:
        remaining_hp = opponent_hp - power
    else: remaining_hp = 0
    print(f'{pokemon_choice.upper()} inflicts {power} damage on opponent\'s {opponent_pokemon_name.upper()}.')
    print(f'Opponent\'s pokemon has {remaining_hp} hp remaining.')
    return remaining_hp

# opponent's random move
def opponent_move():
    random_move_index = random.sample(opponent_pokemon['moves'], 1)
    random_move = random_move_index[0]['move']['name']
    opponent_move = random_move
    opponent_move_url = f'https://pokeapi.co/api/v2/move/{opponent_move}/'
    opponent_move_response = requests.get(opponent_move_url)
    opponent_random_move = opponent_move_response.json()
    if opponent_random_move['power'] == None:
        power = 0
    else: power = int(opponent_random_move['power'])
    if hp - power >= 0:
        remaining_hp = hp - power
    else: remaining_hp = 0
    print(f'Opponent\'s {opponent_pokemon_name.upper()} executes {opponent_move} and inflicts {power} damage on your {pokemon_choice.upper()}.')
    print(f'Your {pokemon_choice.upper()} has {remaining_hp} remaining.')
    return remaining_hp

# some kind of for loop here to keep the battle going until either player_move() == 0 or opponent_move() == 0
# write results to file tallying wins for player and opponent
if player_move() == 0:
    print('You win!')
    # write to file
else: opponent_move()