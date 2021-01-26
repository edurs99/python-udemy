import time
def tail (file,n):
    with open ('sample_file.txt','r') as f:
        # reading the file in a list
        content = f.read().splitlines()
        # getting the last element of the list
        last = content[len(content) -n:]
        print(last)
        # concatenating the list back into a string
        my_str = '\n'.join(last)
        return my_str
while True:
    t = tail('sample_file.txt', 3)
    print(t)
    time.sleep(3)
    print('')