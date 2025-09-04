with open("test.txt", "w") as file:
    lines = ["New Line\n", "New Line\n", "New Line\n"]
    file.writelines(lines)
