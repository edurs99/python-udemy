import csv

people = [
    ['Dan', 34, 'Bucuresti'],
    ['Andrei',21, 'London'],
    ['Maria', 45, 'Paris']
]
# writing in to a file

with open('people2.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=':')
    for item in people:
        writer.writerow(item)

# reading in to a file

with open('people2.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=':')
    for row in reader:
        print(row)
