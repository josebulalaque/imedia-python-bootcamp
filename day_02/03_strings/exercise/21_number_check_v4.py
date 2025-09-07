# Ask the user for an input
user_input = input("Enter number: ")
split_input = user_input.split()
clean = " ".join(split_input)

# TODO: Remove extra spaces
# clean = user_input.strip()
# print(f"spaces cleaned: {clean}")
clean = clean.replace(" ","")

# TODO: Remove commas
clean_comma = clean.replace(",", "")
print(f"commas cleaned: {clean_comma}")

# TODO: Remove extra spaces



# TODO: If user enters a valid number
if clean_comma.isnumeric() or clean_comma[1:].isnumeric():
    clean_comma = int(clean_comma)
    print(f"You entered a valid number {clean_comma}")
else:
    print("Please enter a valid number!")
