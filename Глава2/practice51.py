#!/usr/bin/env python

import math

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Эта прогамма вычисляет корни квадатного уравнения")
    print("f(x) = ax^2 + bx + c")
    a = float(input("Введите коэффициент 'a' :"))
    b = float(input("Введите коэффициент 'b' :"))
    c = float(input("Введите коэффициент 'c' :"))
    Discriminant = b**2 - 4*a*c
    print("Дискриминант равен = %f" % Discriminant)
    if Discriminant < 0:
        print("Уравнение не имеет действительных корней!")
        exit()
    if Discriminant == 0:
        print("Уравнение имеет один действительный корень!")
        root1 = -b / (2*a)
        print("Корень равен = %f" % root1 )
        exit()
    if Discriminant > 0:
        root1 = (-b + Discriminant)/(2*a)
        root2 = (-b - Discriminant)/(2*a)
        print("Первый корень равен = %f" % root1)
        print("Второй корень равен = %f" % root2)
