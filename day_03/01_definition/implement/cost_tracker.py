class CostTracker:
    def __init__(self):
        self.items = []

    def spend(self, item):
        self.items.append(item)
        print(f"ayan gumastos ka ng halagang {item}")

    def refund(self):
        print(f"ayan nagREFUND ka last na gastos mo halagang {self.items[-1]}")
        self.items.pop(-1)

    def show(self):
        return f"eto na ang mga gastos mo ser: {self.items}"

    def total(self):
        return f"eto naman ang total ng gastos mo ser: {sum(self.items)}"

    def save(self):
        with open("expenses.txt", "a") as file:
            for item in self.items:
                file.write(f"{item}\n")
        print(f"Na save ko na sa file ser -> {self.items}")

    def load(self):
        loaded_expenses = []
        with open("expenses.txt", "r") as file:
            file_contents = file.readlines()
        for line in file_contents:
            number = float(line.replace("\n", ""))
            loaded_expenses.append(number)
        print(f"eto lahat ng gastos mo: {loaded_expenses}")
        total = sum(loaded_expenses)
        print(f"eto ang total ng lahat lahat: {total:.2f}")

    def mainloop(self):
        running = True

        while running:
            command = input("Command: ")
            if command == "spend":
                gastos = int(input("Magkano ginastos mo ser: "))
                self.spend(gastos)
            elif command == "refund":
                self.refund()
            elif command == "show":
                print(self.show())
            elif command == "total":
                print(self.total())
            elif command == "save":
                self.save()
            elif command == "load":
                self.load()
            elif command == "exit":
                running = False
            else:
                print("Invalid command")

cost1 = CostTracker()
cost1.mainloop()
