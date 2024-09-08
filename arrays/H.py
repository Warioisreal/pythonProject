f = open('input.txt')
n, m = map(int, f.readline().split())
a = []
for i in range(n * m):
    if i == 0 or i > 0 and i // m != (i - 1) // m:
        a.append([])
    a[i // m].append((i // m) * (i % (n * (m // n) + (m % n))))
f.close()
f1 = open('output.txt', 'w')
for i in range(n * m):
    if i > 0 and i // m != (i - 1) // m:
        f1.write('\n')
    f1.write(f' {a[i // n][i % m]}')
f1.close()
