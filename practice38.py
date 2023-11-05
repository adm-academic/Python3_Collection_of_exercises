#!/usr/bin/env python

import math

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Эта программа определяет название геометрической фигуры по числу её сторон.")
    scount = int(input("введите число сторон фигуры:"))
    if (scount<3) or (scount>10):
        print("Программа не знает фигуру с числом сторон %d " % scount)
    else:
        if scount == 3:
            print("это треугольник")
        elif scount == 4:
            print("это прямоугольник")
        elif scount == 5:
            print("это пентагон")
        elif scount == 6:
            print("это гексагон")
        elif scount == 7:
            print("это семиугольник")
        elif scount == 8:
            print("это октагон")
        elif scount == 9:
            print("это деятиугольник")
        elif scount == 10:
            print("это декагон")