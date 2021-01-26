# with open('devices.txt', 'r') as f:
#     devices = f.read().splitlines()
#     #print(devices)
# # criando uma lista
# mylist = list()
# # criando um for, onde eu defino o campo delimitador e adiciono o conteudo na lista
# for item in devices:
#     tmp = item.split(':')
#     mylist.append(tmp)
# print(mylist)

import csv

with open('devices.txt','r') as f:
    reader = csv.reader(f, delimiter = ':')
    mylist = list()
    for row in reader:
        mylist.append(row)
    print(mylist)