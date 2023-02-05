# Write a program that simulates a lottery. The program should have a list of seven numbers that
# represent a lottery ticket. It should then generate seven random numbers. After comparing the two
# sets of numbers, the program should output a prize based on the number of matches:
# ● £20 for three matching numbers
# ● £40 for four matching numbers
# ● £100 for five matching numbers
# ● £10000 for six matching numbers
# ● £1000000 for seven matching numbers

import random

my_lottery = [4, 8, 15, 16, 23, 42, 69]

lottery_numbers = [
    random.randint(1,99),
    random.randint(1,99),
    random.randint(1,99),
    random.randint(1,99),
    random.randint(1,99),
    random.randint(1,99),
    random.randint(1,99),
]

print("The lottery numbers are {}".format(lottery_numbers))

lottery_items = 0
matches = 0

for lottery_number in lottery_numbers:
    if my_lottery[lottery_items] in lottery_numbers:
        matches = matches + 1
    lottery_items = lottery_items + 1

winnings = [0, 0, 0, 20, 40, 100, 10000, 1000000]

print("You matched {} numbers. You win £{}!".format(matches,winnings[matches]))