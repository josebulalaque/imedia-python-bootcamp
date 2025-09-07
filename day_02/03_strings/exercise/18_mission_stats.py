mission = "Orbiter Alpha"
distance_km = 1500000.4567
days = 92.5
speed = distance_km / (days * 24)
completion = 0.35123

print(" Mission Log ")
print(f"Mission: {mission}")
print(f"Distance: {distance_km:,.2f} km")
print(f"Duration: {days:.2f} days")
print(f"Speed: {speed:.0f} km/h")
print(f"Completion: {completion:.3%}")

# TODO: Follow the given format:
"""
    Mission Log
    Mission: Orbiter Alpha
    Distance: 1,500,000.46 km
    Duration: 92.50 days
    Speed: 675.68 km/h
    Completion: 35.123%
"""
