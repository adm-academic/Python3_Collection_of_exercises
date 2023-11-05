#!/usr/bin/env python

import math

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Эта программа вычисляет объём цилиндра по его радиусу и высоте.")
    r = float(input("Введите радиус цилиндра:"))
    h = float(input("Введите высоту цилиндра:"))
    ploshad_kruga = math.pi * ( r**2 )
    obyom_cilindra = ploshad_kruga * h
    print("Объём цилиндра равен: %.1f" % obyom_cilindra)