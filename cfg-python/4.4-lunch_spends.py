costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
total_cost = 0

for cost in costs:
    total_cost = (total_cost + cost)

print(total_cost)

print(f"{total_cost:.2f}")
print("{:.2f}".format(total_cost))

# easier way is to use sum function rather than for loop

#costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
#total = sum(costs)

#print(total)