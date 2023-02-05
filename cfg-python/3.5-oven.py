oven_temperature = int(input("How hot is the oven? "))

if  oven_temperature > 200:
    print("The oven is too hot")

elif oven_temperature < 150:
    print("The oven is too cold")

elif oven_temperature == 180:
    print("The oven is at the perfect temperature")

else:
    print("The oven is close enough")