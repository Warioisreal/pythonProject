import turtle as tt
"""
Повтори 10 раз
     Сместиться на (4, 3)
     Сместиться на (-4, 10)
     Сместиться на (18, -12)
     Сместиться на (-24, -12)
конец
Перед началом алгоритма Чертёжник находился в точке с координатами (0, 0).
Определите количество точек с целочисленными координатами, которые принадлежат получившейся линии.
"""
tt.left(90)
m = 4
tt.screensize(10000, 10000)
tt.tracer(0)
for i in range(10):
    x1 = tt.xcor() + 4 * m
    y1 = tt.ycor() + 3 * m
    tt.goto(x1, y1)
    x1 = tt.xcor() - 4 * m
    y1 = tt.ycor() + 10 * m
    tt.goto(x1, y1)
    x1 = tt.xcor() + 18 * m
    y1 = tt.ycor() - 12 * m
    tt.goto(x1, y1)
    x1 = tt.xcor() - 24 * m
    y1 = tt.ycor() - 12 * m
    tt.goto(x1, y1)
tt.up()
tt.goto(0, 0)
for x in range(-100, 50):
    for y in range(-110, 50):
        tt.goto(x * m, y * m)
        tt.dot(3, 'black')
tt.goto(0, 0)
tt.dot(3, 'red')
tt.done()
