# original, broken code
chairs = '15'
nails = 4

total_nails = chairs * nails
# solution said: total_nails = int(chairs) * nails

message = 'I need to buy {} nails'.format(total_nails)
print('You need to buy {} nails'.format(message))

# error is that chairs is passed in as a string, not a number

# my new code
chairs = 15
nails = 4

total_nails = chairs * nails

message = 'I need to buy {} nails'.format(total_nails)
print((message))