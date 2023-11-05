#!/usr/bin/env python

import math

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Расчёт некоторых арифметических функций:")
    a = int( input("Введите число (a):") )
    b = int( input("Введите число (b):") )
    print("сумма a и b: %.4f" % (a-b) )
    print("разница между a и b: %.4f" % ( a - b ) )
    print("произведение a и b: %.4f" % ( a * b ) )
    print("частное от деления a на b: %.4f" % (a / b) )
    print("остаток от деления a на b: %.4f" % (a % b) )
    print("десятичный логарифм числа a: %.4f" % (math.log10(a)) )
    print("результат возведения числа a в степень b: %.4f" % (a**b) )