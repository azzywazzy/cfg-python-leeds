import requests

pokemon_number = input("What is the Pokemon's ID? ")

url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)

response = requests.get(url)
pokemon = response.json()
    
print("The pokemon's name is {}".format(pokemon["name"]))
print("The pokemon's height is {}".format(pokemon["height"]))
print("The pokemon's weight is {}".format(pokemon["weight"]))

moves = pokemon["moves"]

for move in moves:
    print("This pokemon has move {}".format(move["move"]["name"]))  