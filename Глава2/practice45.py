#!/usr/bin/env python

import math

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Эта прогамма опеделяет канадские праздники по введённой дате.")
    month = int(input("Введите номер месяца: "))
    day   = int(input("Введите дату  месяце: "))
    if month==1 and day==1:
        print("В эту дату в Канаде празднуют Новый год")
    elif month==7 and day==1:
        print("В эту дату в Канаде празднуют День Канады")
    elif month==12 and day==25:
        print("В эту дату в Канаде празднуют Рождество")
    else:
        print("На дату %02d-%02d не приходится праздников." % (month,day))