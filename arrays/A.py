f = open('input.txt')
n = int(f.readline())
f.close()
A = []
for i in range(n):
    A.append([0] * (n - i - 1) + [1] + [2] * i)
f1 = open('output.txt', 'w')
for i in range(n):
    f1.write(" ".join(str(j) for j in A[i]) + '\n')
f1.close()