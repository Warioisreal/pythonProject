for a in range(1, 100):
    q = 1
    for x in range(1, 100):
        for y in range(1, 100):
            if not((x & 55 == 0) or (x & 10) or (x & a)):
                q = 0
    if q:
        print(a)
        break