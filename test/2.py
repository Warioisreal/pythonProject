'''
Направо 198
Повтори 5 [Вперёд 10 Налево 144]
Определите, сколько различных треугольников содержит фигура, нарисованная Черепахой.

'''
import turtle as tt
m = 10
tt.screensize(2000, 2000)
tt.rt(198)
for i in range(5):
    tt.fd(10 * m)
    tt.lt(144)
'''
tt.up()
tt.tracer(0)
for x in range(-10, 30):
    for y in range(-50, 10):
        tt.goto(x * m, y * m)
        tt.dot(3, 'blue')'''
tt.done()
