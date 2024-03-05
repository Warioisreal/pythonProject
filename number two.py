class Student:
    id_ = 0
    name = ""
    p_id = 0
    cls = ""
    mark = 0


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

for i in range(1, len(stud)):
    x = stud[i]
    j = i - 1
    while j >= 0 and stud[j].mark > x.mark:
        stud[j + 1] = stud[j]
        j -= 1
    stud[j + 1] = x

k, i = 0, len(stud) - 1
x = input()
print(f"{x} класс:")
while k < 3:
    if x in stud[i].cls:
        print(f"{k + 1} место: {stud[i].name.split()[1][0]}. {stud[i].name.split()[0]}")
        k += 1
    i -= 1
