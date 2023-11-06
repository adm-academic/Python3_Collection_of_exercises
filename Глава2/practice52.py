#!/usr/bin/env python

import math

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Эта прогамма переводит буквенные оценки  числовые.")
    balls_l = str(input("Введите буквенную оценку:")).upper()
    balls_n = -1
    if balls_l=="A+" :
        balls_n = 4.0
    elif balls_l=="A" :
        balls_n = 4.0
    elif balls_l=="A-" :
        balls_n = 3.7
    elif balls_l=="B+" :
        balls_n = 3.3
    elif balls_l=="B" :
        balls_n = 3.0
    elif balls_l=="B-" :
        balls_n = 2.7
    elif balls_l=="C+" :
        balls_n = 2.3
    elif balls_l=="C" :
        balls_n = 2.0
    elif balls_l=="C-" :
        balls_n = 1.7
    elif balls_l=="D+" :
        balls_n = 1.3
    elif balls_l=="D-" :
        balls_n = 1.0
    elif balls_l=="F" :
        balls_n = 0
    if balls_n == -1:
        print("Ошибка ввода! Такой символьной оценки не сущестует!")
        exit()

    print("Этой буквенной оценке соотетствует цифровая : %.1f " % balls_n)

