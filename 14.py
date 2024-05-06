def f(a):
s = set()
for j in range(1, int(a ** 0.5) + 1):
if a % j == 0:
s.add(a // j)
s.add(j)
return sorted(s)


k = 0
b = [0, 0]
for i in range(286564, 287270 + 1):
a = f(i)
if len(a) > k:
k = len(a)
b = [a[-1], a[-2]]
print(k, b)
