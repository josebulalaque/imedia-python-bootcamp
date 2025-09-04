prices = [10_000, 20, 3_000, 3, 2, 1_000]

# Change the first, third, and last values to half the price
prices[0] //= 2
prices[2] //= 2
prices[-1] //= 2

# Show the changed list
print(prices)
