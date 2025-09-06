# Expected username and password (you can change the value)
correct_username = "user"
correct_password = "pass"
admin_username = "admin"
admin_password = "admin"

# Enter username and password
username_input = input("Please provide username: ")
password_input = input("Please provide password: ")

# TODO: Notify user if credentials are valid or invalid

if username_input == correct_username and password_input == correct_password:
    print("USER Account. Access granted")
elif username_input == admin_password and password_input == admin_password:
    print("ADMIN Account. Access granted")
else:
    print("Access denied")

#
# if username_input == admin_username:
#     if password_input == admin_password:
#         print("you are ADMIN! Access granted")
#     else:
#         print("you entered the wrong password")
# elif username_input == correct_username:
#     if password_input == correct_password:
#         print("you are USER! Access granted")
#     else:
#         print("you entered the wrong password")
# else:
#     print("you entered the wrong username")
