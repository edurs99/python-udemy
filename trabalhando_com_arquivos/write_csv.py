import csv

with open('people.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    csvdata = (5,'Anne','Amsterdam')
    writer.writerow(csvdata)

# Criando um CSV com numeros e potencias.

with open('numbers.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['x','x**2', 'x**3', 'x**4'])
    for x in range (1,130):
        writer.writerow([x,x**2, x**3, x**4])