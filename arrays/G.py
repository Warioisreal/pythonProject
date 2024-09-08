f = open('input.txt')
n, m = map(int, f.readline().split())
a = []

for i in range(n):
    a.append(list(map(int, f.readline().split())))
f.close()
s = [0, 0, []]
for i in range(n):
    if max(a[i]) > s[0]:
        s[0] = max(a[i])
        s[1] = 1
        s[2] = [i]
    elif max(a[i]) == s[0]:
        s[1] += 1
        s[2].append(i)
f1 = open('output.txt', 'w')
f1.write(f'{s[1]}\n')
for i in s[2]:
    f1.write(f'{i}\n')
f1.close()
