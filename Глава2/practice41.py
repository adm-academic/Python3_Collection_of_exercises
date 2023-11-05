#!/usr/bin/env python

import math

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Программа определяет вид треугольника по длинне его сторон")
    print("Определяет равнобедренный, равносторонний и разностоонний")
    print("Введите длины всех трёх сторон треугольника")
    a = int(input("Введи сторону a:"))
    b = int(input("Введи сторону b:"))
    c = int(input("Введи сторону c:"))
    if a==b and b==c and c==a:
        print("Это равносторонний треугольник")
    elif a==b or b==c or c==a:
        print("Это равнобедренный треугольник")
    elif a!=b and b!=c and c!=a:
        print("Это разносторонний треугольник")