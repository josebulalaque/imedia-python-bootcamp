# Expected password (you can change the value)
correct_password = "pass"

# Enter user password
password_input = input("Please provide password: ")

# TODO: Notify user if password is valid
correct_password_given = correct_password == password_input
print("Access:", correct_password_given)
