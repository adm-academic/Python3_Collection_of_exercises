#!/usr/bin/env python

from math import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Эта программа вычисляет расстояние между двумя координатами на земном шаре " +
          "(широта,долгота) при следовании по кратчайшему пути по поверхности планеты." )
    degree_t1=float( input("широта первой координаты в градусах:") )
    degree_g1=float( input("долгота первой координаты в градусах:") )
    degree_t2 = float(input("широта второй координаты в градусах:"))
    degree_g2 = float(input("долгота второй координаты в градусах:"))
    t1 = radians(degree_t1)
    g1 = radians(degree_g1)
    t2 = radians(degree_t2)
    g2 = radians(degree_g2)
    # in degrees
    distance = 6371.01 * acos(  sin(t1) * sin(t2) + cos(t1)*cos(t2)*cos(g1-g2)  )
    print("После подсчёта кратчайшего расстояния между двумя точками на земном шаре заданным "+
          "в виде коодинат градусах будет равно: %.4f киллометров." % (distance) )