# TODO: Ask the user for three values
expense_1 = int(input("Enter Number1: "))  # Let the user enter a number
expense_2 = int(input("Enter Number2: "))    # Let the user enter a number
expense_3 = int(input("Enter Number3: "))    # Let the user enter a number

# TODO: Then, print each information one line at a time
print(expense_1)
print(expense_2)
print(expense_3)

total = expense_1 + expense_2 + expense_3
print(total)

# TODO: Format this part using f-strings
print(expense_1, "+", expense_2, "+", expense_3, "=", total)
print(f"{expense_1} + {expense_2} + {expense_3} = {total}")


