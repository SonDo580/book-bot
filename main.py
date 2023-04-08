import string

fpath = 'books/frankenstein.txt'

with open(fpath) as fhandle:
    content = fhandle.read()

# print(content)

words = content.split()
words_count = len(words)

letters_count = {}
for letter in content:
    if letter not in string.ascii_letters:
        continue
    letter = letter.lower()
    letters_count[letter] = letters_count.get(letter, 0) + 1