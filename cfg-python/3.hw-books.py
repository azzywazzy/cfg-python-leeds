import random

book_date = int(input("When was the book published? "))

century = (book_date / 100) + 1
decade = book_date % 100

if book_date < 1800 or book_date > 1950:
    print("Please enter a date between 1800 and 1950")

elif decade >= 90:
    decade = "Nineties"
    print("The book is from the {}th century and the {}".format(int(century),decade))

elif decade >= 80:
    decade = "Eighties"
    print("The book is from the {}th century and the {}".format(int(century),decade))

elif decade >= 70:
    decade = "Seventies"
    print("The book is from the {}th century and the {}".format(int(century),decade))

elif decade >= 60:
    decade = "Sixties"
    print("The book is from the {}th century and the {}".format(int(century),decade))

elif decade >= 50:
    decade = "Fifties"
    print("The book is from the {}th century and the {}".format(int(century),decade))

elif decade >= 40:
    decade = "Fourties"
    print("The book is from the {}th century and the {}".format(int(century),decade))

elif decade >= 30:
    decade = "Thirties"
    print("The book is from the {}th century and the {}".format(int(century),decade))

elif decade >= 20:
    decade = "Twenties"
    print("The book is from the {}th century and the {}".format(int(century),decade))

elif decade >= 10:
    decade = "Tens"
    print("The book is from the {}th century and the {}".format(int(century),decade))

else:
    decade = "Noughties"
    print("The book is from the {}th century and the {}".format(int(century),decade))
