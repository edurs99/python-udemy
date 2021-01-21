# metodo com with
with open('a.txt','r') as file:
    file.seek(4)
    word = file.read(5)
    print(word)


# método com open

## Opening the file in read only mode
f = open('a.txt', 'r')

## Move the cursor on position 4 inside the file
f.seek(4)

## Read 5 characters starting with position 4 and return them in variable called word
word = f.read(5)
print(word)

## Closing the file
f.close()