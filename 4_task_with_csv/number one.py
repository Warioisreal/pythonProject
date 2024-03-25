# id, Name, titleProject_id, class, score

f = open("students.csv", encoding="utf8")
a = []
for i in f:
    a.append(i[:-1])
f.close()
name = "Хадаров Владимир"
for i in a:
    if name in i:
        mark = i.split(",")[4][:-1]
        id_ = i.split(",")[2][:-1]
if not mark:
    mark = None
print(f"Ты получил: {mark}, за проект - {id_}")
n = 7
av = [0 for i in range(5)]
for i in a[1:]:
    _ = i.split(",")[3][:-1]
    _1 = i.split(",")[-1]
    if _1.isdigit():
        av[int(_) - n] += int(_1)
f1 = open("student_new.csv", "w", encoding="utf8")
for i in a:
    if not i.split(",")[-1]:
        f1.write(i + str(av[int(i.split(",")[3]) - n]) + "\n")
f1.close()
