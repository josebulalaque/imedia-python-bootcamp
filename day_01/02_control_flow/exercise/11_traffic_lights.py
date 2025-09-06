# Ask the user input for a color
color_input = input("Please enter a color: ")

# TODO: Print the following depending on the color input
# "green"   -> print "Go"
# "yellow"  -> print "Wait..."
# "red"     -> print "Stop"

if color_input == "red":
    print("You picked red color. STOP!!!")
elif color_input == "yellow":
    print("You picked yellow color. WAIT!!!")
elif color_input == "green":
    print("You picked green color. GO!!!")
else:
    print("You picked other color. TERMINATING PROGRAM!!!")

