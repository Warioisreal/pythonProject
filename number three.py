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
p_id = input()
while p_id != "СТОП":
    if p_id.isdigit():
        q = 0
        for i in stud:
            if int(p_id) == i.p_id:
                print(f"Проект № {i.p_id} делал: {i.name.split()[1][0]}. {i.name.split()[0]} он(а) получил(а) оценку - {i.mark}")
                q = 1
        if not q:
            print("Ничего не найдено")
    p_id = input()
if p_id == "СТОП":
    print("Хорошего дня!")