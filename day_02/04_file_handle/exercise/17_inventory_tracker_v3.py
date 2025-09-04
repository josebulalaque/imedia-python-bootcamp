def add(inventory, item):
    """Add a new item (dict) to the inventory (list[dict])"""
    inventory.append(item)


def remove(inventory, index):
    """Remove item (dict) in the given index (int) of inventory"""
    return inventory.pop(index)


def read(inventory, index):
    """Return the item (dict) in the given index (int) of inventory"""
    return inventory[index]


def show(inventory):
    """Print the items and their details line-by-line"""
    if not inventory:
        print("Inventory is empty.\n")
        return

    for number, info_detail in enumerate(inventory, start=1):
        print(f"Item {number}:")

        for key, value in info_detail.items():
            print(f"\t{key}: {value}")


def save(inventory, filepath):
    """TODO: Save the inventory (list[dict]) to a filepath"""


def load(filepath):
    """TODO: Return a list[dict] from a filepath"""


def main():
    running = True
    inventory = []

    while running:
        command = input("Command: ").strip().lower()

        if command == "add":
            item_name = input("Item name: ")
            item_info = input("Item info: ")
            item = {"Name": item_name, "Info": item_info}
            add(inventory, item)
            print(f"{item} added to inventory\n")

        elif command == "remove":
            index = int(input("Index (remove): "))
            removed_item = remove(inventory, index - 1)  # user-friendly 1-based index
            print(f"{removed_item} removed from inventory\n")

        elif command == "read":
            index = int(input("Index (read): "))
            item = read(inventory, index - 1)  # user-friendly 1-based index
            print(f"Item {index}: {item}\n")

        elif command == "show":
            show(inventory)

        elif command == "save":
            filepath = input("Filepath: ")
            save(inventory, filepath)

        elif command == "load":
            filepath = input("Filepath: ")
            inventory = load(filepath)

        elif command == "exit":
            running = False
            print("Exiting...")


main()
