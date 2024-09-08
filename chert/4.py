import turtle as tt
"""
сместиться на (0, 12)
сместиться на (5, -12)
сместиться на (-10, 0)
сместиться на (5, 12)
сместиться на (0, 4)
сместиться на (3, -4)
сместиться на (-6, 0)
сместиться на (3, 4)
Найдите разность между максимальным и минимальным периметром нарисованных треугольников.

"""
tt.left(90)
m = 20
tt.screensize(10000, 10000)

x1 = tt.xcor() + 0 * m
y1 = tt.ycor() + 12 * m
tt.goto(x1, y1)

x1 = tt.xcor() + 5 * m
y1 = tt.ycor() - 12 * m
tt.goto(x1, y1)

x1 = tt.xcor() - 10 * m
y1 = tt.ycor() + 0 * m
tt.goto(x1, y1)

x1 = tt.xcor() + 5 * m
y1 = tt.ycor() + 12 * m
tt.goto(x1, y1)

x1 = tt.xcor() + 0 * m
y1 = tt.ycor() + 4 * m
tt.goto(x1, y1)

x1 = tt.xcor() + 3 * m
y1 = tt.ycor() - 4 * m
tt.goto(x1, y1)

x1 = tt.xcor() - 6 * m
y1 = tt.ycor() + 0 * m
tt.goto(x1, y1)

x1 = tt.xcor() + 3 * m
y1 = tt.ycor() + 4 * m
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
