# Ask the user input for a color
color_input = input("Please enter a color: ")

# TODO: Print the following depending on the color input
# "green"   -> print "Go"
# "yellow"  -> print "Wait..."
# "red"     -> print "Stop"
# Everything else   -> print "Malfunction"

match color_input:
    case "red":
        print("You picked red color. STOP!!!")
    case "yellow":
        print("You picked yellow color. WAIT!!!")
    case "green":
        print("You picked green color. GO!!!")
    case _:
        print("You picked other color. MALFUNCTION!!!")
