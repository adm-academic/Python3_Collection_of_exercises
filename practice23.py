#!/usr/bin/env python

import math

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Многоугольник называется правильным, если все его стороны и углы равны.")
    print("Площадь такой фигуры можно вычислить по следующей формуле " + \
          "в которой s – длина стороны, а n – количество сторон:")
    s = float(input("Введите длинну стороны: "))
    n = float(input("Введите количество сторон: "))
    area = (n*(s**2)) / (4*math.tan(math.pi/n))
    print("Площадь такого многоугольника будет равна: %.2f " % area)