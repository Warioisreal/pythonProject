n = input()
Len = len(n)
coll = Len - int(input())
# глобальная переменная строка n
# локальная переменная-аргумент это coll это количество символов в отобранной строке
result = []
# индекс первого символа в оптимальной выборке
pos = 0
while coll > 0 and pos < Len:

    max_id = pos

    for i in range(pos, Len):
        if n[max_id] == "9":
            break
        if Len - i < coll:
            break
        if n[i] > n[max_id]:
            max_id = i

    result.append(n[max_id])
    pos = max_id + 1
    coll -= 1
    max_id += 1

for i in result:
    print(i, end="")