#!/usr/bin/env python

import math

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Эта программа переводит градусы Цельсия в градусы Фаренгейта и Кельвина.")
    celsius = float(input("Введите температуру в градусах Цельсия:"))
    fahrenheit = celsius*9/5+32
    kelvin = celsius + 273.15
    print("%.2f Цельсия будет %.2f Фаренгейта" % (celsius,fahrenheit) )
    print("%.2f Цельсия будет %.2f Кельвина" % (celsius,kelvin) )