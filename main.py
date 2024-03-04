def tr(a, b, c):
    return a + b > c and a + c > b and b + c > a


for g in range(1, 1000):
    q = 0
    for y in range(1, 1000):
        if not((not(tr(y, 11, 16) == (not(max(y, 5) > 10)))) and tr(4, g, y)):
            q = 1
    if not q:
        print(g)
