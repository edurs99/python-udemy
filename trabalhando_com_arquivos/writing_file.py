# criando arquivos no modo append

with open('myfile1.txt','a') as f:
    f.write('\nabc\n')
    f.write('just a 2nd line\n')

# criando arquivos no modo read and write

with open('configuration.txt','r+') as file:
    file.write('Line added with r+\n')
