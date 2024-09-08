def f1(a):
    a = '_' + a
    s = ''
    arr = []
    for i in range(1, len(a)):
        if a[i - 1] != a[i]:
            s += a[i]
            arr.append(0)
        arr[-1] += 1
    return s, arr


def f2(a):
    return sum(a) - max(a) - min(a)


s1 = input()
s2 = input()
s3 = input()
su1, ct1 = f1(s1)
su2, ct2 = f1(s2)
su3, ct3 = f1(s3)
if su1 == su2 == su3:
    for i in range(len(su1)):
        print(su1[i] * f2([ct1[i], ct2[i], ct3[i]]), end='')
else:
    print('IMPOSSIBLE')
