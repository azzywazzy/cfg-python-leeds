# In this session you used the Pokemon API to retrieve a single Pokemon. I want a program that can
# retrieve multiple Pokemon and save their names and moves to a file.
# Use a list to store about 6 Pokemon IDs. Then in a for loop call the API to retrieve the data for each
# Pokemon. Save their names and moves into a file called 'pokemon.txt'

import requests

field_names = ["number", "name", "moveset"]

pokemon_numbers= [
    int(input("Please enter the number of the first Pokemon: ")),
    int(input("Please enter the number of the second Pokemon: ")),
    int(input("Please enter the number of the third Pokemon: ")),
    int(input("Please enter the number of the fourth Pokemon: ")),
    int(input("Please enter the number of the fifth Pokemon: ")),
    int(input("Please enter the number of the sixth Pokemon: ")),
]

count = 0

for pokemon_number in pokemon_numbers:
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_numbers[count])

    response = requests.get(url)
    pokemon = response.json()     
    
    moves = pokemon["moves"]

#dictionary
    # data = [
    #     {
    #         "number": pokemon_numbers[count], 
    #         "name": pokemon["name"], 
    #         "moveset": moves[0]["move"]["name"],
    #         }
    # ]

#list
    data = [
        pokemon_numbers[count], 
        pokemon["name"], 
        moves[0]["move"]["name"],
]

    print(data)
    count = count + 1

with open("pokemon.txt", "w+") as text_file:

    text_file.write(data)

