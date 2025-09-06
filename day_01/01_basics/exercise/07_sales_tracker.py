#ask the cost and pax or count for three separate items
item_cost_1 = int(input("Enter S26 Gold price: "))
item_count_1 = int(input("Enter how many items: "))
print(f"Ang total price ng Gatas ng Baby ay {item_cost_1 * item_count_1}")
item_cost_2 = int(input("Enter Diaper price: "))
item_count_2 = int(input("Enter how many items: "))
print(f"Ang total price ng Diaper ay {item_cost_2 * item_count_2}")
item_cost_3 = int(input("Enter Mineral Water price: "))
item_count_3 = int(input("Enter how many items: "))
print(f"Ang total price ng Mineral Water ay {item_cost_3 * item_count_3}")

#calculate the total
total = (item_cost_1 * item_count_1) + (item_cost_2 * item_count_2) + (item_cost_3 * item_count_3)
#print(total)

print(f"Ang S26 Gold ay {item_cost_1 * item_count_1}, ang Diaper ay {item_cost_2 * item_count_2}, ang Mineral Water ay {item_cost_3 * item_count_3}. And overall total ay {total}")




