# TODO: Ask the user for an integer input
number = int(input("Pick a number: "))
count = int(input("Pick how many items: "))

print(f"You picked number {number} to be multiplied up to {count} times.")

for items in range(1, count+1):
    print(f"{number} x {items} = {number * items}")

# TODO: Print the multiplication table for that number
"""
Example:
number = 3

3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30
"""
