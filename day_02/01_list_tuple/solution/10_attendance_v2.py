attendee_names = []

attendee_count = int(input("Attendee count: "))

for _ in range(attendee_count):
    attendee_name = input("Attendee name: ")
    attendee_names.append(attendee_name)

# Remove your name in attendees (if it’s there)
your_name = "jeff"
if your_name in attendee_names:
    attendee_names.remove(your_name)

print(attendee_names)
