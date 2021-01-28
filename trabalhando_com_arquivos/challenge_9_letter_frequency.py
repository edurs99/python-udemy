
## OPCAO 1 - COM ITERACAO NA VARIVEL COM SPLITLINES

import string

letters = dict()

# initializing the dictionary with all letters as keys and zero as values
for c in string.ascii_lowercase:
    letters[c] = 0
#print(letters)

with open('american_english.txt', 'r') as words:
    content = words.read().splitlines()
    for w in content:
        for char in string.ascii_lowercase:
            letters[char] += w.count(char)
print(letters)

## OPCAO 2 - COM ITERACAO NA VARIVEL DO NOME DO ARQUIVO

import string

letters = dict()

# initializing the dictionary with all letters as keys and zero as values
for c in string.ascii_lowercase:
    letters[c] = 0
#print(letters)

with open('american_english.txt', 'r') as words:
    for w in words:
        for char in string.ascii_lowercase:
            letters[char] += w.count(char)
print(letters)