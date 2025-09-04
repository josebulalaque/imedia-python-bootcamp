string = "I am perfectly calm and everything is fine"

lower_case_count = 0
upper_case_count = 0
space_count = 0

for char in string:
    if char.islower():
        lower_case_count += 1
    elif char.isupper():
        upper_case_count += 1
    elif char.isspace():
        space_count += 1

# Print the number of lowercase, uppercase, and spaces.
print("Lower case count:", lower_case_count)
print("Upper case count:", upper_case_count)
print("Space count:", space_count)
