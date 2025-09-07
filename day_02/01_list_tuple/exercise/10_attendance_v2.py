attendee_names = []

attendee_count = int(input("Attendee count: "))

# TODO: For every attendee expected:
# TODO: Add attendee_name to attendee_names

for count in range(attendee_count):
    attendee_name = input(f"Attendee name {count+1}: ")
    attendee_names.append(attendee_name)

print(f"ATTENDANCE LIST: {attendee_names}")

# TODO: Remove your name in attendees (if it’s there)

choice = input("Would you like to remove names? (Y/N [default:N]): ")
if choice in ("Y", "y"):
    remove_name = input("Remove name: ")
    if remove_name in attendee_names:
        attendee_names.remove(remove_name)
        print(f"UPDATED LIST: {attendee_names}")
    else:
        print(f"{remove_name} NOT FOUND: ")
        print(f"ATTENDANCE LIST: {attendee_names}")

input("Press Enter to continue...")
var = attendee_names.pop(-1)
print(f"REMOVING LAST ATTENDEE {var}")
print(f"UPDATED LIST: {attendee_names}")

