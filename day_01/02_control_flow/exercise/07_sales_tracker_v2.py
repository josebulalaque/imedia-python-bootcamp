# TODO: Ask the user how many items will be calculated
input_count = int(input("Enter the number of items:"))
total = 0

# TODO: Use a for loop to ask for more than one cost and count
for count in range(input_count):
        item_cost = int(input(f"Enter Item {count+1} cost: "))  # Let the user enter a number
        item_count = int(input(f"Enter number of items: "))  # Let the user enter a number
        item_total = item_cost * item_count
        print(f"Item {count+1} total: {item_total}")
        total += item_total
print(f"\nOVERALL TOTAL: {total}")
