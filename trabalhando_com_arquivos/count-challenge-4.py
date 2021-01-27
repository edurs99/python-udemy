def wc(file):
    with open (file,'r') as f:
        # reading the file in a list
        content = f.read().splitlines()
        # atribuindo a qtde de linhas a variavel lines
        lines = len(content)
        # contando as qtde de palavras existentes em cada linha
        words = 0
        for line in content:
            words += len(line.split())
        chars = 0
        for line in content:
            chars += len(list(line))
        return lines, words, chars
print(wc('sample_file.txt'))
