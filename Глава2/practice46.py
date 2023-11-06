#!/usr/bin/env python

import math

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Эта программа определяет цвет шахматной клетки по её координате")
    print("Проверка на правильность введённой координаты не производится")
    coords = str(input("Введите шахматные координаты:"))
    letter = coords[0].lower()
    digit = int(coords[1])
    is_white = (ord(letter) + digit) % 2
    if is_white :
        print("По координате %s расположена белая клетка." % coords)
    else:
        print("По координате %s расположена чёрная клетка." % coords)