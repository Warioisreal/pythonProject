for i in range(50):
    f = '0' + i * '12' + '0'
    while not '00' in f:
        if '011' in f:
            f = f.replace('011', '101', 1)
        else:
            f = f.replace('01', '40', 1)
            f = f.replace('02', '20', 1)
            f = f.replace('0222', '1401', 1)
    if f.count('1') == 6 and f.count('2') == 9:
        print(f)
