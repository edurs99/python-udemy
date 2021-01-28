# with open('american_english.txt', 'r') as f:
#     content = f.read().splitlines()
#     print(content)
# mylist = list()
# # criando um for, onde eu defino o campo delimitador e adiciono o conteudo na lista
# chars = 0
# for item in content:
#     tmp = item.split(',')
#     chars = len(list(item))
#     mylist.append(tmp)
#     mylist.append(chars)
# print(mylist)

with open('american_english.txt') as f:
    words = f.read().splitlines()

    #print(words)
    words_and_length = dict()
    for w in words:
        words_and_length[w] = len(w)

    print(words_and_length)

    for primeiro, segundo in words_and_length.items():
         print(f'{primeiro} -> {segundo}')