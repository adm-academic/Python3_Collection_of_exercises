#!/usr/bin/env python

from math import floor

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Эта программа определяет с какого дня недели начался указанный год!")
    year = 2023
    day_of_the_week = (  year + floor((year - 1) / 4)
                              - floor((year - 1) / 100)
                              + floor((year - 1) / 400)
                       ) % 7
    if day_of_the_week == 0:
        print("Воскресенье")
    elif day_of_the_week == 1:
        print("Понедельник")
    elif day_of_the_week == 2:
        print("Вторник")
    elif day_of_the_week == 3:
        print("Среда")
    elif day_of_the_week == 4:
        print("Четверг")
    elif day_of_the_week == 5:
        print("Пятница")
    elif day_of_the_week == 6:
        print("Суббота")