from sre_constants import CHCODES


chocolates = {
    'white': 1.50,
    'milk': 1.20,
    'dark': 1.80,
    'vegan': 2.00,
}

order = input("What would you like to buy? white/milk/dark/vegan? ")

print("The price of {} chocolate is £{}".format(order, chocolates[order]))