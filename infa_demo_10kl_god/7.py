for a in range(-100, 100):
    q = 1
    for x in range(1, 100):
        for y in range(1, 100):
            if not((2 * y - x < a) or (x + 2 * y > 50) or (2 * x + y < 40)):
                q = 0
    if q:
        print(a)
        break