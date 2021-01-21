# lendo arquivos e atribuindo diretamente em listas


with open('configuration.txt','r') as file:
    my_list = file.read().splitlines()
    print(my_list)

# lendo arquivos e colocando em listar com <enter>
with open('configuration.txt','r') as file:
    my_list = file.readlines()
    print(my_list)

# o objeto file é iterável...entao, consigo ler linha a linha cada vez q dou print

with open('configuration.txt','r') as file:
    print(file.readline())
    print(file.readline())

# iterando com for
with open('configuration.txt', 'r') as file:
    for line in file:
        print(line, end ='')
