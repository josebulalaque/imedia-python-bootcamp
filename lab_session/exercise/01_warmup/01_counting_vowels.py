def count_vowels(string: str) -> int:
    """Return the number of vowels in the given string"""
    x=0
    for char in string.lower():
        if char in 'aeiou':
            x += 1
    return x

print(count_vowels("ABCDeeeerrrefef"))

