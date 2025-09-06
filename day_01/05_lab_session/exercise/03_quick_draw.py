from random import choice

while True:
    options = ["rock","paper","scissors"]
    cpu_choice = choice(options)

    # Ask the user for an input
    user_choice = input("Pick a choice (rock/paper/scissors): ")

    if user_choice == cpu_choice:
        print(f"You chose {user_choice}, CPU chose {cpu_choice}, result: DRAW!")
    elif user_choice == "rock" and cpu_choice == "paper":
        print(f"You chose {user_choice}, CPU chose {cpu_choice}, result: CPU WON!")
    elif user_choice == "paper" and cpu_choice == "scissors":
        print(f"You chose {user_choice}, CPU chose {cpu_choice}, result: CPU WON!")
    elif user_choice == "scissors" and cpu_choice == "rock":
        print(f"You chose {user_choice}, CPU chose {cpu_choice}, result: CPU WON!")
    elif user_choice == "rock" and cpu_choice == "scissors":
        print(f"You chose {user_choice}, CPU chose {cpu_choice}, result: USER WON!")
    elif user_choice == "paper" and cpu_choice == "rock":
        print(f"You chose {user_choice}, CPU chose {cpu_choice}, result: USER WON!")
    elif user_choice == "scissors" and cpu_choice == "paper":
        print(f"You chose {user_choice}, CPU chose {cpu_choice}, result: USER WON!")
    else:
        print("You chose wrong option!")

    retry=input(f"Do you want to try again [y/n]?: ")
    if retry == "y":
        continue
    elif retry == "n":
        break
    else:
        print("wrong input! exiting")
        break

# TODO: Make a random choice for the computer
# Note: Read the slide for this part

# TODO: Determine if the user wins, the cpu wins, or its a draw

# Challenge: TODO: Robust Input
# Challenge: TODO: Multi-rounds
