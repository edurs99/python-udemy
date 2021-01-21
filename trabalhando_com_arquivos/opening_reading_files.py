# lendo arquivos com metodo open. é necessário fechar o arquivo depois do final da tarefa

f = open('configuration.txt','r')
content = f.read()
print(content)

print(f.closed)
f.close()
print(f.closed)

# lendo apenas os primeiros 5 caracteres do arquivo

f = open('configuration.txt','r')
content = f.read(5)
print(content)

# como o python guarda a posicao na memoriam se formos ler os proximos 3 caracteres, ele continua de onde parou

content = f.read(3)
print(content)
# para verificar a posicao do cursos, use o comando tell

print(f.tell())

# para mudar para uma posicao especifica, use seek

f.seek(8)
print(f.read(7))

# para voltar para o comeco do file
f.seek(0)
print(f.read(1))
f.close()


