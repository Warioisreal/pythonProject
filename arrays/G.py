f = open('input.txt')
n, m = map(int, f.readline().split())
a = []

for i in range(n):
    a.append(list(map(int, f.readline().split())))
f.close()
s = [0, 0]
for i in range(n):
    if max(a[i]) > s[0]:
        s = [max(a[i]), 1]
    elif max(a[i]) == s[0]:
        s[1] += 1
f1 = open('output.txt', 'w')
f1.write(f'{s[1]}')
f1.close()