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

def save(expenses):
    """TODO: Save the current list of expenses to a new file"""
    with open("expenses.txt", "a") as file:
        for expense in expenses:
            file.write(f"{expense}\n")

    print(f"Na save ko na sa file ser -> {expenses}")

def load():
    loaded_expenses = []
    with open("expenses.txt", "r") as file:
        file_contents = file.readlines()
    for line in file_contents:
        number = float(line.replace("\n", ""))
        loaded_expenses.append(number)
    print(f"eto lahat ng gastos mo: {loaded_expenses}")
    total = sum(loaded_expenses)
    print(f"eto ang total ng lahat lahat: {total:.2f}")

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
        elif command == "save":
            save(current_expenses)
        elif command == "load":
            load()
        elif command == "exit":
            running = False
        else:
            print("Invalid command")


main()
