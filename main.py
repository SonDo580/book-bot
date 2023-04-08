import sys
import string

if len(sys.argv) != 2:
    print('Usage: python main.py <file_name>')
    exit(1)

fname = sys.argv[1]
try:
    with open(fname) as fhandle:
        content = fhandle.read()
except Exception as e:
    print(e)
    exit(1)

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

def print_report(filename, words_count, letters_count):
    print(f'--- Begin report of {filename} ---')
    print(f'{words_count} words found in the document\n')

    letters_list = list(letters_count)
    letters_list.sort()

    for letter in letters_list:
        print(f"The '{letter}' character was found {letters_count[letter]} times")

    print('--- End report ---')

words_count = count_words(content)
letters_count = count_letters(content)
print_report(fname, words_count, letters_count)