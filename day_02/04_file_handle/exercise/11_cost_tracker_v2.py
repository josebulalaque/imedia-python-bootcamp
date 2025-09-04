def spend(expenses):
    """TODO: Add a new cost in expenses"""


def refund(expenses):
    """TODO: Remove the last cost added (if any)"""


def show(expenses):
    """TODO: Print the current list of expenses and total"""


def save(expenses):
    """TODO: Save the current list of expenses to a new file"""


def main():
    running = True
    current_expenses = []

    while running:
        command = input("Command: ")
        if command == "spend":
            spend(current_expenses)


main()
