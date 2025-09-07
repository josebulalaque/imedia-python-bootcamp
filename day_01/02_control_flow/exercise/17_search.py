items = ["rice", "noodles", "toyo", "spam", "coffee"]
item_to_find = "spam"

for item in items:
    # TODO: If item equals the item_to_find, print and exit loop
    if item == item_to_find:
        print(f"found it!: {item}")
        continue
    print(f"current value: {item}")

if item_to_find in items:
    print(f"found it!: {item_to_find}")
else:
    print(f"nothing found!: {item_to_find}")
