invited = {"Ana", "Ben", "Carlo", "Dani"}
attended = {"Ben", "Carlo", "Ely"}

# TODO: Who are all the involved members?
print("Involved Members:")
print(invited.union(attended))

# TODO: Who was absent?
print("Absent:")
print(invited.difference(attended))

# TODO: Who gatecrashed?
print("Not enrolled but attended:")
print(attended.difference(invited))

# TODO: Who was invited and attended
print("Attended properly:")
print(attended.intersection(invited))