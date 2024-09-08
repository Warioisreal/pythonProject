import turtle as tt
tt.tracer(0)
tt.screensize(10000, 10000)
m = 10
for i in range(15):
    x1 = tt.xcor() + 10 * m
    y1 = tt.ycor() + 10 * m
    tt.goto(x1, y1)

    x1 = tt.xcor() + 3 * m
    y1 = tt.ycor() + -6 * m
    tt.goto(x1, y1)

    x1 = tt.xcor() + -9 * m
    y1 = tt.ycor() + 3 * m
    tt.goto(x1, y1)

tt.up()
tt.goto(0, 0)
tt.dot(5, 'red')
for x in range(-20, 20):
    for y in range(-20, 20):
        tt.goto(x * m, y * m)
        tt.dot(3)
print(13 * 15)
tt.done()
