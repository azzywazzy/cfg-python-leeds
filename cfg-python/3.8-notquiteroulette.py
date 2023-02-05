import random

bet_amount = float(input("How much would you like to bet? £"))
bet_colour = input("What colour would you like to bet on? red/black ")
bet_number = int(input("What number would you like to bet on? Between 1 and 100 "))

def colour():
    random_number = random.randint(1, 2)

    if random_number == 1:
        colour = 'red'
    else:
        colour = 'black'

    return colour


random_number = random.randint(1, 100)
random_colour = colour()

print("Random number was {}".format(random_number))
print("Random colour was {}".format(random_colour))

if  bet_colour == random_colour:
    print("You've won £{}".format(bet_amount * 2))

elif bet_number == random_number:
    print("You've won £{}".format(bet_amount * 2))

elif  bet_colour and bet_number == random_colour and random_number:
    print("You've won £{}".format(bet_amount * 100))

else:
    print("You've won nothing")

