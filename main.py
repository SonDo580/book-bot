import string

fpath = 'books/frankenstein.txt'

with open(fpath) as fhandle:
    content = fhandle.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letters_count = {}
    for letter in text:
        if letter not in string.ascii_letters:
            continue
        letter = letter.lower()
        letters_count[letter] = letters_count.get(letter, 0) + 1
    return letters_count
    
words_count = count_words(content)
letters_count = count_letters(content)