import turtle as tt
"""
ПОВТОРИ 7 РАЗ
     сместиться на (6, -9)
     сместиться на (-6, 2)
     сместиться на (12, 3)
КОНЕЦ ПОВТОРИ
Определите, сколько различных точек с целочисленными координатами принадлежат траектории Чертёжника,
считая начальную и конечную точки, если исполнитель стартует в точке с целочисленными координатами.
"""
tt.left(90)
m = 15
tt.screensize(10000, 10000)
tt.tracer(0)
for i in range(7):
    x1 = tt.xcor() + 6 * m
    y1 = tt.ycor() - 9 * m
    tt.goto(x1, y1)
    x1 = tt.xcor() - 6 * m
    y1 = tt.ycor() + 2 * m
    tt.goto(x1, y1)
    x1 = tt.xcor() + 12 * m
    y1 = tt.ycor() + 3 * m
    tt.goto(x1, y1)
tt.up()
tt.goto(0, 0)
for x in range(-10, 100):
    for y in range(-50, 50):
        tt.goto(x * m, y * m)
        tt.dot(5, 'black')
tt.goto(0, 0)
tt.dot(5, 'red')
tt.done()
