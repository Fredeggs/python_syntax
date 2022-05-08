aList = ['hi', 'hello', 'ebola', 'smargleflarg', 'nuts', 'Eggs', 'bolts']

def print_upper_words(words):
    """Accepts a list of strings. Prints and capitalizes each string on its own line"""
    for word in words:
        print(word.upper())

# print_upper_words(aList)

def print_e_words(words):
    """Accepts a list of strings. Only prints the strings that start with 'e'"""
    for word in words:
        first_letter = word[0].upper()
        if first_letter == 'E':
            print(word)

# print_e_words(aList)

def print_words(words, letters):
    """Accepts a list of strings and a set of letters. Only prints the strings that start with letters in the inputted set"""
    for word in words:
        first_letter = word[0].upper()
        for letter in letters:
            if letter.upper() == first_letter:
                print(word.upper())

print_words(["hello", "hey", "goodbye", "yo", "yes"],
                   letters={"h", "y"})
