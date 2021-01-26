with open ('sample_file.txt','r') as f:
    # reading the file in a list
    reader = f.read().splitlines()
    print(reader)
    # concatenating the list back into a string
    my_string = '\n'.join(reader)
    print(my_string)