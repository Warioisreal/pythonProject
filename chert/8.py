import turtle as tt
"""
Повтори 10 раз
     Сместиться на (3,6)
     Сместиться на (7,-2)
     Сместиться на (-10,-4)
Конец
Перед началом алгоритма Чертёжник находился в точке с координатами (0, 0).
Определите, сколько точек с целочисленными координатами будут находиться внутри области, ограниченной линией,
заданной данным алгоритмом. Точки на линии учитывать не следует.
"""
tt.left(90)
m = 50
tt.screensize(10000, 10000)

for i in range(1):
    x1 = tt.xcor() + 3 * m
    y1 = tt.ycor() + 6 * m
    tt.goto(x1, y1)
    x1 = tt.xcor() + 7 * m
    y1 = tt.ycor() - 2 * m
    tt.goto(x1, y1)
    x1 = tt.xcor() - 10 * m
    y1 = tt.ycor() - 4 * m
    tt.goto(x1, y1)

tt.up()
tt.tracer(0)
tt.goto(0, 0)
for x in range(-10, 100):
    for y in range(-50, 50):
        tt.goto(x * m, y * m)
        tt.dot(5, 'black')
tt.goto(0, 0)
tt.dot(5, 'red')
tt.done()
