# Expected username and password (you can change the value)
correct_username = "user"
correct_password = "pass"

# Enter username and password
username_input = input("Please provide username: ")
password_input = input("Please provide password: ")

# TODO: Notify user if credentials are valid or invalid
correct_credentials = correct_password == password_input
correct_username = correct_username == username_input

if correct_credentials and correct_username:
    print("Access granted")
else:
    print("Access denied")

