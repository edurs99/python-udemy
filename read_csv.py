import csv
with open('airtravel.csv', 'r') as f:
    reader = csv.reader(f)
# Removendo o titulo do CSV
    next(reader)
    year_1958 = dict()
    year_1959 = dict()
    year_1968 = dict()
    for row in reader:
# imprimindo todo o conteudo do arquivo
#      print(row)
# imprimir o a coluna 0 no dicionario qdo imprimir a coluna 1
# este = nao é de atrubuicao, e sim de comparacao (true/false)
        year_1958[row[0]] = row[1]
# imprimindo demais anosprint(year_1958)
        year_1959[row[0]] = row[2]
        year_1968[row[0]] = row[3]

#print(year_1958)
#print(year_1959)

#print(year_1968)

# imprimindo maior valor

max_1958 = max(year_1958.values())
#print(max_1958)

# imprimindo o valor apurado acima, rolando toda a lista.

for k, v in year_1958.items():
    if max_1958 == v:
        print(f'Busiest Month in 1958:{k}, Flights: {v.strip()}')