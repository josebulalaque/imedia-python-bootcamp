# Ask the user for an input
user_input = input("Enter number: ")

# TODO: Remove extra spaces
clean = user_input.strip()
print(clean)

# TODO: If user enters a valid number
if user_input.isnumeric() or user_input[1:].isnumeric():
    user_input = int(user_input)
    print(user_input+1)
else:
    print("Please enter a valid number!")
