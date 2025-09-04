def add(inventory, item):
    """TODO: Add a new item (dict) to the inventory (list[dict])"""


def remove(inventory, index):
    """TODO: Remove item (dict) in the given index (int) of inventory"""


def read(inventory, index):
    """TODO: Return the item (dict) in the given index (int) of inventory"""


def show(inventory):
    """TODO: Print the items and their details line-by-line"""


def main():
    running = True
    inventory = []

    while running:
        command = input("Command: ")
        if command == "add":
            # TODO: Use add command"""
            pass
        elif command == "remove":
            #  TODO: Use remove command"""
            pass
        elif command == "read":
            # TODO: Use read command"""
            pass
        elif command == "show":
            # TODO: Use show command"""
            pass
        elif command == "exit":
            running = False


main()
