import turtle as tt
"""
Повтори N раз
     Сместиться на (4, 3)
     Сместиться на (-5, 10)
     Сместиться на (6, -6)
     Сместиться на (-5, -8)
конец
Перед началом алгоритма Чертёжник находился в точке с координатами (0, 0).
Определите минимальное значение N, при котором линия, оставленная Чертежником, пройдет через начало координат 2 раза.
Факт расположения исполнителя в начале координат перед запуском алгоритма не учитывать.

"""
tt.left(90)
m = 20
tt.screensize(10000, 10000)

for i in range(13):
    x1 = tt.xcor() + 4 * m
    y1 = tt.ycor() + 3 * m
    tt.goto(x1, y1)
    x1 = tt.xcor() - 5 * m
    y1 = tt.ycor() + 10 * m
    tt.goto(x1, y1)
    x1 = tt.xcor() + 6 * m
    y1 = tt.ycor() - 6 * m
    tt.goto(x1, y1)
    x1 = tt.xcor() - 5 * m
    y1 = tt.ycor() - 8 * m
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
