import sys
a = int(input())
b = int(input())
c = int(input())
D = (b ** 2) - (4 * a * c)
if a==0:
    print("Уравнение не квадратное")
    sys.exit(0)
if D >= 0:
    x1 = (-b + D ** 0.5) / (2 * a)
    x2 = (-b - D ** 0.5) / (2 * a)
    print(x1, x2)
else:
    print("корней нет")
