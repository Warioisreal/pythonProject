import turtle as tt
"""
Повтори 13 раз
     Сместиться на (6,3)
     Сместиться на (-6,2)
     Сместиться на (-4,-1)
     Сместиться на (4,-4)
конец
Определите, площадь области, ограниченной линией, заданной данным алгоритмом. 
В ответе укажите только целую часть полученного значения.

"""
tt.left(90)
m = 20
tt.screensize(10000, 10000)

for i in range(13):
    x1 = tt.xcor() + 6 * m
    y1 = tt.ycor() + 3 * m
    tt.goto(x1, y1)
    x1 = tt.xcor() - 6 * m
    y1 = tt.ycor() + 2 * m
    tt.goto(x1, y1)
    x1 = tt.xcor() - 4 * m
    y1 = tt.ycor() - 1 * m
    tt.goto(x1, y1)
    x1 = tt.xcor() + 4 * m
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
