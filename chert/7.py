import turtle as tt
"""
Повтори 2 раз
     Сместиться на (3, 4)
     Сместиться на (-3, 4)
     Сместиться на (-3, -4)
     Сместиться на (3, -4)
конец
Найдите минимальную длину линии, которой можно нарисовать эту фигуру.
"""
tt.left(90)
m = 20
tt.screensize(10000, 10000)

for i in range(2):
    x1 = tt.xcor() + 4 * m
    y1 = tt.ycor() + 3 * m
    tt.goto(x1, y1)
    x1 = tt.xcor() - 3 * m
    y1 = tt.ycor() + 4 * m
    tt.goto(x1, y1)
    x1 = tt.xcor() - 3 * m
    y1 = tt.ycor() - 4 * m
    tt.goto(x1, y1)
    x1 = tt.xcor() + 3 * m
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
