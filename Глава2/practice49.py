#!/usr/bin/env python

import math

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Эта программа определяет животное по китайскому гороскопу.")
    year = int(input("Введите год: "))
    if year % 12 == 8:
        animal = "Дракон"
    elif year % 12 == 9:
        animal = "Змея"
    elif year % 12 == 10:
        animal = "Лошадь"
    elif year % 12 == 11:
        animal = "Коза"
    elif year % 12 == 0:
        animal = "Обезьяна"
    elif year % 12 == 1:
        animal = "Петух"
    elif year % 12 == 2:
        animal = "Собака"
    elif year % 12 == 3:
        animal = "Свинья"
    elif year % 12 == 4:
        animal = "Крыса"
    elif year % 12 == 5:
        animal = "Бык"
    elif year % 12 == 6:
        animal = "Тигр"
    elif year % 12 == 7:
        animal = "Кролик"
    print("По китайскому гороскопу год %d принадлежит животному: %s." % (year, animal))