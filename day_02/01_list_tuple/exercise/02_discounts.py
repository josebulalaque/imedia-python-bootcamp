prices = [10_000, 20, 3_000, 3, 2, 1_000]

# TODO: Change the first, third, and last values to half the price

# Show the changed list
print(prices)

indices = [0,2,-1]

print(indices)

for index in indices:
    prices[index] = prices[index]/2
    print((prices[index]))
