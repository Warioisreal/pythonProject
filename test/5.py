'''
Повтори 4 [ Повтори 3 [ Вперед 2 Направо 270] Вперед 5]
Найдите минимальную площадь выпуклого многоугольника, включающего фигуру.

'''
import turtle as tt
m = 20
tt.screensize(2000, 2000)
for i in range(4):
    for j in range(3):
        tt.fd(2 * m)
        tt.rt(270)
    tt.fd(5 * m)

tt.up()
tt.tracer(0)
for x in range(-10, 30):
    for y in range(-50, 10):
        tt.goto(x * m, y * m)
        tt.dot(3, 'blue')
tt.done()
