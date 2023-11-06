#!/usr/bin/env python

import math
from random import randrange

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Эта программа симулиует игру в рулетку.")
    # Симулируем запуск рулетки, используя число 37 для представления номера 00
    value = randrange(0, 38)
    if value == 37:
        print("Выпавший номер: 00...")
    else:
        print("Выпавший номер: %d..." % value)
    # Отображаем выигрыш для одного числа
    if value == 37:
        print("Выигравшая ставка: 00")
    else:
        print("Pay", value)
    # Отображаем выигрыш по цветам
    # В первой строке проверяем число на вхождение в ряд 1, 3, 5, 7 и 9
    # Во второй строке проверяем число на вхождение в ряд 12, 14, 16 и 18
    # В третьей строке проверяем число на вхождение в ряд 19, 21, 23, 25 и 27
    # В четвертой строке проверяем число на вхождение в ряд 30, 32, 34 и 36
    if value % 2 == 1 and value >= 1 and value <= 9 or \
            value % 2 == 0 and value >= 12 and value <= 18 or \
    value % 2 == 1 and value >= 19 and value <= 27 or \
    value % 2 == 0 and value >= 30 and value <= 36:
        print("Выигравшая ставка: красное")
    elif value == 0 or value == 37:
        pass
    else:
        print("Выигравшая ставка: черное")
    # Отображаем выигрыш по чет/нечет
    if value >= 1 and value <= 36:
        if value % 2 == 1:
            print("Выигравшая ставка: нечетное")
        else:
            print("Выигравшая ставка: четное")
    # Отображаем выигрыш по низ/верх
    if value >= 1 and value <= 18:
        print("Выигравшая ставка: от 1 до 18")
    elif value >= 19 and value <= 36:
        print("Выигравшая ставка: от 19 до 36")