def is_strong_password(password: str) -> bool:
    """
    Returns True if the password meets the following criteria:
    - At least 8 characters
    - Contains at least one digit
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    """
    ctr_digit=0
    ctr_upper=0
    ctr_lower=0

    if len(password) > 8:
        for char in password:
            if char.isdigit():
                ctr_digit+=1
            if char.isupper():
                ctr_upper+=1
            if char.islower():
                ctr_lower+=1
    else:
        return False


    print("CTR digit:", ctr_digit)
    print("CTR upper:", ctr_upper)
    print("CTR lower:", ctr_lower)
    return None


print(is_strong_password("Pass.12345123"))

