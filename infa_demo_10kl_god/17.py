f = open('input.txt')
a = f.read().replace('XYZ', '*')
f.close()
k, mx = 0, 0
for i in a:
    if i == '*':
        k += 1
    else:
        mx = max(k, mx)
        k = 0
print(mx * 3)
