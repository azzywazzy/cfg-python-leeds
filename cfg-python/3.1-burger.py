# Can I afford the burger

#burger_price = input("What is the price of a burger?")

#within_budget = float(burger_price) <= 10.00

#print("The burger is within budget: {}" .format(within_budget))

# Is the restaurant suitable?

#burger_price = input("What is the price of a burger?")
#has_veggie = input("Is there a vegetarian option? y/n")

#within_budget = float(burger_price) <= 10.00
#is_suitable = has_veggie == "y"

#can_visit = within_budget and is_suitable

#print("Restaurant meets criteria: {}" .format(can_visit))

# Rewriting to use IF statements

#burger_price = input("What is the price of a burger?")
#affordable = float(burger_price) <= 10.00

#has_veggie = input("Is there a vegetarian option? y/n ")
#is_suitable = has_veggie == "y"

#if affordable and is_suitable:
#    print("This restaurant is a great choice")

#if not affordable or not is_suitable:
#    print("Probably not a good idea")

# Other option creating a combined parameter

#burger_price = input("What is the price of a burger?")
#affordable = float(burger_price) <= 10.00

#has_veggie = input("Is there a vegetarian option? y/n ")
#is_suitable = has_veggie == "y"

#can_visit =  affordable and is_suitable

#if  can_visit:
#    print("This restaurant is a great choice")

#if not can_visit:
#    print("Probably not a good idea")

# Using else statement

#burger_price = input("What is the price of a burger?")
#affordable = float(burger_price) <= 10.00
#has_veggie = input("Is there a vegetarian option? y/n ")
#is_suitable = has_veggie == "y"

#if affordable and is_suitable:
#    print("This restaurant is a great choice")

#else:
#    print("Probably not a good idea")

# discount

meal_price = float(input("How much did the meal cost? "))

discount_choice = input("Do you have a discount? y/n ")
discount_applicable = discount_choice == "y"

if meal_price > 20.00 and discount_applicable:
    meal_price = meal_price * 0.9
    print("Discount applied")
else:
    print("No discount")

print("Total cost: {}". format(meal_price))