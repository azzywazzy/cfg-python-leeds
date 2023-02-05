import random

first_names = ['bart', 'lisa', 'maggie']
last_names = ['simpson','flanders', 'schmo']
verbs = ['skates', 'eats', 'drinks']
nouns = ['ice', 'potatoes', 'milkshakes']

chosen_firstname = random.choice(first_names)
chosen_lastname = random.choice(last_names)
chosen__verb = random.choice(verbs)
chosen_noun = random.choice(nouns)

print('{} {} {} {}'.format(chosen_firstname, chosen_lastname, chosen__verb, chosen_noun))

