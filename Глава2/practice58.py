#!/usr/bin/env python

import math

def eto_nevisokonyi(year):
    nevisokosnyi = True
    if (year % 400) == 0:
        nevisokosnyi = False
        return nevisokosnyi
    elif (year % 100) == 0:
        nevisokosnyi = True
        return nevisokosnyi
    elif (year % 4) == 0:
        nevisokosnyi = False
        return nevisokosnyi
    return nevisokosnyi


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Определяет високосный год или не високосный.")
    year = int(input("Введите год от нашей эры:"))
    if eto_nevisokonyi(year):
        print("Это НЕвисокосный год!")
    else:
        print("Это Високосный год!")