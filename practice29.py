#!/usr/bin/env python

import math

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Эта программа рассчитывает коэффициент охлаждения ветром.")
    T = float(input("Введите температуру по термометру:"))
    V = float(input("Введите скорость ветра:"))
    WCI = 13.12 + 0.6215*T + 11.37*math.pow(V,0.16) + 0.3965*T*math.pow(V,0.16)
    print("Коэффициент охлаждения ветром равен %.6f " % (WCI) )