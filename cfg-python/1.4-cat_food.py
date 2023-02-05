cats = 10
cans = 2
days = 7

total_cans = cats * cans * days

# concatenating strings
output = str(cats) + " cats eat " + str(total_cans) + " total cans over " + str(days) + " days"
print(output)


# using .format() to insert numbers from variables instead
output = "{} cats eat {} total cans over {} days" .format(cats, total_cans, days)
print(output)


# also could use f string
output = f"{cats} cats eat {total_cans} total cans over {days} days"
print (output)

