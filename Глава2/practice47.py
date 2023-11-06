#!/usr/bin/env python

import math

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Эта программа определяет время года по дате")
    month = int(input("Введите номер месяца года:"))
    if month>0 and month<=2:
        print("Зима")
    elif month>=3 and month<=5:
        print("Весна")
    elif month>=6 and month<=8:
        print("Лето")
    elif month>=9 and month<=11:
        print("Осень")
    elif month==12:
        print("Зима")
    else:
        print("Такого месяца не существует!")