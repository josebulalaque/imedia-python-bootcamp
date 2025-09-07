banned_words = ("moist", "break", "raise")

# TODO: Ask the user for a word
# TODO: If the word is in banned_words, say "Banned"

while True:
    response = input("Input a word: ")
    if response in banned_words:
        print("THOU SHALL NOT PASS!")
    else:
        print("OKE GO!")