# TODO: Ask the user for an input that should be a number

while True:
    number = input("Enter number: ")

    # Then try to convert this into an integer using the following:
    try:
        number_converted = int(number)
        if number_converted < 0:
            raise ValueError()
        print("You entered a Number!")
    except ValueError:
        print("We don’t accept strings or negatives!")

    retry=input(f"Do you want to try again [y/n]?:")
    if retry == "y":
        continue
    elif retry == "n":
        break
    else:
        print("wrong input! exiting")
        break



# The user could provide an invalid integer input (string)
# TODO: Handle this case

# The user could give a negative number
# TODO: Handle this case

# Challenge: TODO: Give the user infinite times to retry
