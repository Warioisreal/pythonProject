f = open('input.txt')
n, m = map(int, f.readline().split())
a = []

for i in range(n):
    a.append(list(map(int, f.readline().split())))
f.close()
s = [0, 0]
for i in range(n):
    if sum(a[i]) > s[0]:
        s = [sum(a[i]), i]
f1 = open('output.txt', 'w')
f1.write(str(s[0]) + "\n")
f1.write(str(s[1]))
f1.close()