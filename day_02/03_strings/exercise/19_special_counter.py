string = input('Enter string: ')
special_count = 0
special_char = '!@#$%^&*()'

# TODO: Add one to special_count for each special char in string
for char in string:
    if char in special_char:
        special_count += 1

print(special_count)
