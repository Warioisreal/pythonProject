import turtle as tt
tt.tracer(0)
m = 30
for i in range(10):
    tt.fd(6 * m)
    tt.rt(120)
tt.up()
tt.goto(0, 0)
tt.dot(5, 'red')
for x in range(-10, 10):
    for y in range(-10, 10):
        tt.goto(x * m, y * m)
        tt.dot(3)
tt.done()