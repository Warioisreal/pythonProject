'''
Повтори 10 [Налево 60 Вперёд 300 Налево 60]
Определите, сколько точек с целочисленными координатами будут находиться внутри области,
ограниченной линией, заданной данным алгоритмом. Точки на линии следует учитывать.

'''
k = 0
for x in range(-500, 10):
    for y in range(-200, 200):
        if x >= -150 * 3 ** 0.5 and x / 3 ** 0.5 <= y <= -x / 3 ** 0.5:
            k += 1
print(k)