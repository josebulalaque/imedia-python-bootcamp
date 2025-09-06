total = 0
running = True
while running:
    command = input("Provide command: ")

    if command == "add":
        number = int(input("Enter number: "))
        total += number
        print(f"total is: {total}") # Ask for number, add to total, and print
    if command == "sub":
        number = int(input("Enter number: "))
        total -= number
        print(f"total is: {total}")  # Ask for number, subtract to total, and print

    if command == "check":
        print(f"CURRENT total is: {total}")

    if command == "clear":
        total = 0
        print(f"CLEARED! current total is: {total}")

    if command == "exit":
        running = False
