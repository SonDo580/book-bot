fpath = 'books/frankenstein.txt'

with open(fpath) as fhandle:
    content = fhandle.read()

print(content)