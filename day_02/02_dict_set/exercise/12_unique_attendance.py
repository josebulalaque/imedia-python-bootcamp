attendee_names = set()

attendee_count = int(input("Attendee count: "))

# TODO: For every attendee expected:
# TODO: Add attendee_name to attendee_names
for count in range(attendee_count):
    attendee_name = input(f"Attendee name {count+1}: ")
    attendee_names.add(attendee_name)

print(f"ATTENDANCE LIST: {attendee_names}")

