# lendo arquivos com metodo open. é necessário fechar o arquivo depois do final da tarefa

f = open('configuration.txt','r')
content = f.read()
print(content)

print(f.closed)
f.close()
print(f.closed)