import random


class Student:
    id_ = 0
    name = ""
    p_id = 0
    cls = ""
    mark = 0


def Login(c):
    return f"{c.split()[0]}_{c.split()[1][0]}{c.split()[2][0]}"


def Password():
    letters = "abcdefghijklmnopqrstuvwxyz" + "abcdefghijklmnopqrstuvwxyz".upper() + "0123456789"
    return ''.join(random.choice(letters) for _ in range(8))


f = open("student_new.csv", encoding="UTF8")
a = []
stud = []
for i in f:
    a.append(i[:-1])
f.close()
for i in range(1, len(a)):
    stud.append(Student())
    stud[i - 1].id_ = int(a[i].split(",")[0])
    stud[i - 1].name = a[i].split(",")[1]
    stud[i - 1].p_id = int(a[i].split(",")[2])
    stud[i - 1].cls = a[i].split(",")[3]
    stud[i - 1].mark = float(a[i].split(",")[4])
    stud[i - 1].login = Login(stud[i - 1].name)
    stud[i - 1].password = Password()

f1 = open("students_password.csv", "w", encoding="UTF8")
f1.write(a[0] + ",login,password" + "\n")
for i in stud:
    f1.write(f"{i.id_},{i.name},{i.p_id},{i.cls},{i.mark},{i.login},{i.password}\n")
f1.close()