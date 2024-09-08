def f(a, b, k):
    if a > b or k > 4: return 0
    elif a == b: return 1
    else:
        if b == 140: return f(a + 3, b, k + 1) + f(a * 4, b, k) + f(a * 5, b, k)
        else: return f(a + 3, b, k) + f(a * 4, b, k) + f(a * 5, b, k)


print(f(1, 16, 0) * f(16, 140, 0) * f(140, 725, 0))
