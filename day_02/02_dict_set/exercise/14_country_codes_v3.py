# TODO: Add more country codes
country_codes = {
    "PH": "Philippines",
    "US": "United States",
    "AU": "Australia",
    "CA": "Canada",
    "SG": "Singapore",
}

# TODO: Print the country for the given country code
# TODO: # If the key is not found, print Unknown

while True:
    country_code = input("Enter country code: ")
    print(f"Country code: {country_codes.get(country_code, 'Unknown')}")
