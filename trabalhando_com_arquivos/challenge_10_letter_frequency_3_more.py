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
    word_list = sorted(letters.items(), key=lambda x: x[1], reverse=True)
    print(word_list[:3])
