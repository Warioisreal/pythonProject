class Student:
    id_ = 0
    name = ""
    p_id = 0
    cls = ""
    mark = 0


f = open("students.csv", encoding="UTF8")
a = []
stud = []
for i in f:
    a.append(i[:-1])
f.close()
s, k = [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
for i in range(1, len(a)):
    stud.append(Student())
    stud[i - 1].id_ = int(a[i].split(",")[0])
    stud[i - 1].name = a[i].split(",")[1]
    stud[i - 1].p_id = int(a[i].split(",")[2])
    stud[i - 1].cls = a[i].split(",")[3]
    m = a[i].split(",")[4]
    if m.isdigit():
        stud[i - 1].mark = int(m)
        s[int(stud[i - 1].cls[:-1]) - 7] += int(m)
        k[int(stud[i - 1].cls[:-1]) - 7] += 1
for i in stud:
    if not i.mark:
        i.mark = int((s[int(i.cls[:-1]) - 7] / k[int(i.cls[:-1]) - 7]) * 1000) / 1000
name = input()
for i in stud:
    if name in i.name:
        print(f"Ты получил: {i.mark}, за проект - {i.p_id}")
