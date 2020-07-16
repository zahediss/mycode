# Inside of your core.py file, create a function named silly_strings
# The silly_strings function should take one parameter, a list of strings

# example words
words = ["Sam", "is", "a", "duck"]

#Pig latin generator
VOWELS = ('a', 'e', 'i', 'o', 'u')


def silly_strings(stringy):
    txt = ""
    for word in stringy:
        if word.startswith(VOWELS):
            txt += f"{word}ay "
        else:
            txt += f"{word[1:]}{word[:1]}ay "
    return(txt)
