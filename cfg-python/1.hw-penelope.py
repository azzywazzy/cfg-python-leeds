# original, broken code
my_name = Penelope
my_age = 29

message = 'My name is {} and I am {} years old'.format(my_name, my_age)
print(message)

# error is that my_name isn't being passed in as a string - needs to be in quotations

# my new code
my_name = 'Penelope'
my_age = 29

message = 'My name is {} and I am {} years old'.format(my_name, my_age)
print(message)