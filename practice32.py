#!/usr/bin/env python

import math

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Программа считает сумму цифр в четырёхзначном числе.")
    chislo = int(input("Введите целое положительное четырёхзначное число:"))
    x1 = chislo % 10
    chislo = chislo // 10
    x2 = chislo % 10
    chislo = chislo // 10
    x3 = chislo % 10
    chislo = chislo // 10
    x4 = chislo % 10
    summa = x4 + x3 + x2 +x1
    print ("Сумма цифр в этом числе равна %d " % summa )