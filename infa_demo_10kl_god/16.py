n, m = map(int, input().split())
a = []
s, k = 0, 0
for i in range(n):
    a.append(list(map(int, input().split())))
    sb = sum(a[i])
    if sb > s:
        s = sb
        k = i
print(s, k + 1)
