import csv

# Lendo um arquivo com delimitaores diferentes de virgula
# with open('passwd.txt','r') as f:
#     reader = csv.reader(f,delimiter = ':', lineterminator = '\n')
#     for row in reader:
#         print(row )
#
# print(csv.list_dialects())

csv.register_dialect('hashes',delimiter='#',quoting=csv.QUOTE_NONE,lineterminator='\n')

with open('items.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, dialect='hashes')

    for row in reader:
        print(row)

# escrevendo uma nova linha no arquivo CSV

with open ('items.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(('spoon', 3, 1,5))
