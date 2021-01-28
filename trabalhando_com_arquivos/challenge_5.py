
with open('banking.txt','r') as f:
    content = f.read().splitlines()
    #print(content)
    deposit, withdrawal = 0, 0

    for item in content:
        tmp = item.split(':')
        print(tmp)
        if tmp[0] =='D':
            deposit += int(tmp[1])
        elif tmp[0] == 'W':
            withdrawal +=int(tmp[1])
        else:
            print('File Format error')
    balance = deposit - withdrawal
    print(balance)