#!/usr/bin/env python

import math

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Эта прогамма вычисляет прощадь круга и объём шара по заданному радиусу.")
    r = float( input("Введите радиус r:") )
    circle_area = math.pi*(r**2)
    sphere_volume = (4/3)*math.pi*(math.pow(r,3))
    print("Площадь круга при радиусе %.2f равна %.2f " % (r,circle_area) )
    print("Объём сферы при радиусе %.2f равен %.2f " % (r, sphere_volume))