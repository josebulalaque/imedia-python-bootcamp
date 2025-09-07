def spend(expenses):
    """TODO: Add a new cost in expenses"""
    gastos = int(input("Magkano ginastos mo ser: "))
    expenses.append(gastos)
    print(f"eto na mga ginastos mo ser {expenses}")

def refund(expenses):
    """TODO: Remove the last cost added (if any)"""
    try:
        var=expenses.pop(-1)
        print(f"narefund mo eto {var}, inalis ko na sa listahan")
    except IndexError:
        print(f"Wala kang gastos, wala kang marerefund wala ka kaseng pera")

def show(expenses):
    """TODO: Print the current list of expenses and total"""
    print(f"eto ang naman ginastos mo {expenses}")
    print(f"eto na naman ang total {sum(expenses)}")


def main():
    running = True
    current_expenses = []

    while running:
        command = input("Command: ")
        if command == "spend":
            spend(current_expenses)
        elif command == "refund":
            refund(current_expenses)
        elif command == "show":
            show(current_expenses)
        else:
            print("Invalid command")


main()
