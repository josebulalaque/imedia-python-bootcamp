import string

def reverse_string(string: str):
    """Return a reversed version of `string`"""
    y = len(string)
    char=""
    for i in range(len(string)):
        char+=string[0-(i+1)]
    return char

print(reverse_string("Hello World"))
