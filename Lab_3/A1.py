x1 = int(input("Введите x1: "))
y1 = int(input("Введите y1: "))
x2 = int(input("Введите x2: "))
y2 = int(input("Введите y2: "))

if x1 > 0 and y1 > 0:
    q1 = 1
elif x1 < 0 and y1 > 0:
    q1 = 2
elif x1 < 0 and y1 < 0:
    q1 = 3
else:
    q1 = 4

if x2 > 0 and y2 > 0:
    q2 = 1
elif x2 < 0 and y2 > 0:
    q2 = 2
elif x2 < 0 and y2 < 0:
    q2 = 3
else:
    q2 = 4

if q1 == q2:
    print("Yes,", ["I", "II", "III", "IV"][q1 - 1])
else:
    print("No")
