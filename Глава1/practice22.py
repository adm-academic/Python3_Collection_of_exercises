#!/usr/bin/env python

import math

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Эта программа рассчитывает площадь треугольника на основании длин всех трех его сторон")
    s1 = float(input("Введите сторону s1:"))
    s2 = float(input("Введите сторону s2:"))
    s3 = float(input("Введите сторону s3:"))
    so = (s1 + s2 + s3) / 2
    area = math.sqrt(so * (so-s1) * (so-s2) * (so-s3))
    print("Площадь треугольника равна: %.2f" % area)