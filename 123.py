s = {"I": 1,
     "II": 2,
     "III": 3,
     "IV": 4,
     "V": 5,
     "VI": 6,
     "VII": 7,
     "VIII": 8,
     "IX": 9,
     "X": 10,
     "XX": 20,
     "XXX": 30,
     "XL": 40,
     "L": 50,
     "LX": 60,
     "LXX": 70,
     "LXXX": 80,
     "XC": 90,
     "C": 100,
     "CC": 200,
     "CCC": 300,
     "CD": 400,
     "D": 500,
     "DC": 600,
     "DCC": 700,
     "DCCC": 800,
     "CM": 900,
     "M": 1000,
     "MM": 2000,
     "MMM": 3000
     }
Sum = 0
a = [i for i in input()]
i = 0
k = 0
while i < len(a) - 5:
    print("11", i)
    if a[i] == a[i + 1]:  # повторка
        k += 1
    if s[a[i]] // 10 == s[a[i + 1]] and s[a[i]] == s[a[i + 2]]:  # 14 или 19
        Sum += s[a[i]] * (k + 1) - s[a[i + 1]]
        k = 0
        i += 2
    if s[a[i]] * 10 == s[a[i + 1]] and s[a[i]] == s[a[i + 2]]:  # 4 или 9
        Sum += s[a[i + 1]] - s[a[i]]
        i += 1
    if s[a[i]] // 10 == s[a[i + 1]] == s[a[i + 2]] != s[a[i + 3]]:  # 11 или 16
        Sum += s[a[i]] * (k + 1) + s[a[i + 1]]
        k = 0
        i += 1
    if s[a[i]] // 10 == s[a[i]] == s[a[i + 2]] == s[a[i + 3]] != s[a[i + 4]]:  # 12 или 17
        Sum += s[a[i]] * (k + 1) + s[a[i + 1]] * 2
        k = 0
        i += 2
    if s[a[i]] // 10 == s[a[i]] == s[a[i + 2]] == s[a[i + 3]] == s[a[i + 4]] != s[a[i + 5]]:  # 13 или 18
        Sum += s[a[i]] * (k + 1) + s[a[i + 1]] * 3
        k = 0
        i += 3
    i += 1
# осталось от 2 до 4 символов
if s[a[i]] * 10 == s[a[i + 1]] and s[a[i]] == s[a[i + 2]]:  # 4 или 9
    Sum += s[a[i + 1]] - s[a[i]]
if a[i] == a[i + 1]:  # повторка
    Sum += s[a[i]] * 2
print("s", Sum)

"""
<problem.png>
XIIV = 15
XIIVIII = 18
XIIIIV = 17
"""
