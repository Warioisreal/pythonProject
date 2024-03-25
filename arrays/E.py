f = open('input.txt')
n, m = map(int, f.readline().split())
a = []

for i in range(n):
    a.append(list(map(int, f.readline().split())))
f.close()
s = [0, 0, 0]
for i in range(n):
    if s[0] < max(a[i]):
        s = [max(a[i]) ,sum(a[i]), i]
    elif s[0] == max(a[i]):
        if s[1] < sum(a[i]):
            s = [max(a[i]) ,sum(a[i]), i]
f1 = open('output.txt', 'w')
f1.write(f'{s[2]}')
f1.close()