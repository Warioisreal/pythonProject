import turtle as tt
"""
ПОВТОРИ 15 РАЗ
     сместиться на (10, 10)
     сместиться на (3, -6)
     сместиться на (-9, 3)
КОНЕЦ ПОВТОРИ
Определите, сколько точек с целочисленными координатами окажутся строго внутри замкнутых треугольных областей,
образованных линией, оставленной Чертёжником, если исполнитель стартует в точке с целочисленными координатами.

"""
tt.left(90)
m = 20
tt.screensize(10000, 10000)

for i in range(15):
    x1 = tt.xcor() + 10 * m
    y1 = tt.ycor() + 10 * m
    tt.goto(x1, y1)
    x1 = tt.xcor() + 3 * m
    y1 = tt.ycor() - 6 * m
    tt.goto(x1, y1)
    x1 = tt.xcor() - 9 * m
    y1 = tt.ycor() + 3 * m
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
