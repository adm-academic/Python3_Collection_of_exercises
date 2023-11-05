#!/usr/bin/env python

import math

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Это программа для расчета индекса массы тела (body mass index –BMI) человека.")
    weight = float(input("Введите массу человека в киллограммах :"))
    height = float(input("Введите рост человека метрах :"))
    BMI = weight/(height**2)
    print("Индекс массы тела равен: %.6f" %  BMI)