attendee_names = set()

attendee_count = int(input("Attendee count: "))

for number in range(1, attendee_count + 1):
    attendee_name = input(f"Attendee {number} name: ")
    attendee_names.add(attendee_name)

# Remove your name from attendees (if there)
your_name = "Jeff"
attendee_names.discard(your_name)

print(attendee_names)
