with open('devices.txt', 'r') as f:
    devices = f.read().splitlines()
    #print(devices)
# criando uma lista
mylist = list()
# criando um for, onde eu defino o campo delimitador e adiciono o conteudo na lista
for item in devices:
    tmp = item.split(':')
    mylist.append(tmp)
print(mylist)
