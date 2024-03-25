f = open('input.txt')
n, m = map(int, f.readline().split())
a = []

for i in range(n):
    a.append(list(map(int, f.readline().split())))
f.close()
s = [0, 0, 0]
for i in range(n):
    for j in range(m):
        if a[i][j] > s[0]:
            s = [a[i][j], i, j]
f1 = open('output.txt', 'w')
f1.write(f'{s[0]}\n')
f1.write(f'{s[1]} {s[2]}')
f1.close()