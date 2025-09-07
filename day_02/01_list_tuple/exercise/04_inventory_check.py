inventory = ("Mousepad", "Keyboard", "Monitor", "Cable")

# TODO: Print the items in the inventory and the order they appear:
"""
    Item 1: Mousepad
	Item 2: Keyboard
	Item 3: Monitor
	Item 4: Cable
"""

for index, name in enumerate(inventory, start=1):
	print(f"Item {index}: {name}")