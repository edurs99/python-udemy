
with open('american_english.txt') as f:
    words = f.read().splitlines()

    #print(words)
    words_and_length = dict()
    for w in words:
        words_and_length[w] = len(w)
    # print words em lengh
    word_list = sorted(words_and_length.items(), key=lambda x: x[1], reverse=True)
    print(word_list[:100])
