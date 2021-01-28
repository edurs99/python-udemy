import csv

people = [
    ['Dan', 34, 'Bucuresti'],
    ['Andrei',21, 'London'],
    ['Maria', 45, 'Paris']
]
# writing in to a file

with open('people1.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    for item in people:
        writer.writerow(item)

# reading in to a file

with open('people1.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
