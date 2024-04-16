'''
Повтори 100 [Вперёд 10 Направо 48]
Определите, сколько отрезков проведёт Черепаха до возврата в исходную точку?


'''
import turtle as tt
m = 10
tt.tracer(1)
tt.screensize(2000, 2000)
tt.lt(90)
for i in range(100):
    tt.fd(10 * m)
    tt.lt(48)
'''
tt.up()
tt.tracer(0)
for x in range(-10, 30):
    for y in range(-50, 10):
        tt.goto(x * m, y * m)
        tt.dot(3, 'blue')'''
tt.done()
