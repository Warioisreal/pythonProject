n = [int(i) for i in input()]
k = int(input())

result = []

arr = [[] for i in range(10)]
for i in range(len(n)):
    arr[n[i]].append(i)

points = [0 for i in range(10)]

for i in range(len(n)):
    a = n[i]
    arr[a].append(i)

pos = 0

while k > 0:
    for i in range(9, 0, -1):
        if len(arr[i]) <= points[i]:  # указатель по цифре прошёл все адреса этой цифры -> переходим к следующей
            continue

        while arr[i][points[i]] < pos:  # дойти до ближайшего справа к указателю или до последнего адреса этой цифры
            points[i] += 1
            if points[i] >= len(arr[i]):
                break

        if len(arr[i]) <= points[i]:  # указатель по цифре прошёл все адреса этой цифры -> переходим к следующей
            continue
        # если после данного адреса >= k символов, то
        # 1) добавляем эту цифру в результат
        # 2) сдвигаем указатель на адрес + 1
        # 3) уменьшаем необходимую длину
        if len(n) - arr[i][points[i]] >= k:
            result.append(i)
            pos = arr[i][points[i]] + 1
            k -= 1
            break

for i in result:
    print(i, end="")
