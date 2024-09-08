f = open('input.txt')
n = int(f.readline())
flag = 0
a = []
for i in range(n):
    a.append(list(map(int, f.readline().split())))
f.close()
for i in range(n):
    for b in range(n):
        if a[b][i] != a[i][b]:
            flag = 1
f1 = open('output.txt', 'w')
f1.write('yes' if flag == 0 else 'no')
f1.close()
