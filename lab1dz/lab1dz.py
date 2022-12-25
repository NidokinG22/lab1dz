import sys
print("Введите коэфиценты уравнения")
a = int(input("a="))
b=int(input("b="))
c=int(input("c="))
D = (b ** 2) - (4 * a * c)
if a==0:
    print("Уравнение не квадратное")
    sys.exit(0)
if D >= 0:
    x1 = (-b + D ** 0.5) / (2 * a)
    x2 = (-b - D ** 0.5) / (2 * a)
    print("Корни уравнения:","x1=",x1,"x2=",x2)
else:
    print("У уравнения корней нет")
