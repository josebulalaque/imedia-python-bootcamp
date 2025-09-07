def add(inventory, item):
    """TODO: Add a new item (dict) to the inventory (list[dict])"""
    inventory.append(item)

def remove(inventory, index):
    """TODO: Remove item (dict) in the given index (int) of inventory"""
    inventory.pop(index)

def read(inventory, index):
    """TODO: Return the item (dict) in the given index (int) of inventory"""
    return inventory[index]

def show(inventory):
    for item in inventory:
        print(f"Items:")
        for key, value in item.items():
            print(f"\t{key}: {value}")

    """TODO: Print the items and their details line-by-line"""

def main():
    running = True
    inventory = []

    while running:
        command = input("Command: ")
        if command == "add":
            name = input("Name: ")
            info = input("Info: ")
            price = input("Price: ")
            dict1 = {"Name": name, "Info": info, "Price": price}
            add(inventory, dict1)
        elif command == "remove":
            index = input("Index: ")
            remove(inventory, int(index))
        elif command == "read":
            index = input("Index: ")
            item = read(inventory, int(index))
            for key, value in item.items():
                print(f"\t{key}: {value}")
        elif command == "show":
            show(inventory)
        elif command == "exit":
            running = False

main()
