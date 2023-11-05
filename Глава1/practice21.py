#!/usr/bin/env python

import math

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Эта программа вычисляет площадь треугольника по основанию и высоте.")
    b = float(input("длина основания треугольника: "))
    h = float(input("высота: "))
    area = ( b * h ) / 2
    print( "Площадь треугольника равна: %.2f" % area )