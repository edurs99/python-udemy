with open ('sample_file.txt','r') as f:
    # reading the file in a list
    content = f.read().splitlines()
    linhas = len(content)

    words = 0
    for line in content:
        words += len(line.split())

    print(words)
    #caracteres = content.count()
    print(linhas)
        # print(last)
        # # concatenating the list back into a string
        # my_str = '\n'.join(last)
        # return my_str
