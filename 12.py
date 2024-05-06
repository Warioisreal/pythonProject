def f1(a):
su, sp = set(), set()
for j in map(int, a.split(';')):
n = len(su)
su.add(j)
if len(su) == n:
sp.add(j)
return len(su) == 4 and len(sp) == 1 and sum(su) < list(sp)[0] * 4


f = open('Задание 11.csv')
k = 0
for i in f:
if f1(i):
k += 1
print(k)
f.close()
