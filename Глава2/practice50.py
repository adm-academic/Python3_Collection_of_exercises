#!/usr/bin/env python

import math

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Эта программа выводит описание силы землятясения по шкале Рихтера по введённым баллам.")
    balls = float(input("Ввведите баллы землятясения по шкале Рихтера:"))
    if balls < 2.0:
        print("Минимальное")
    elif balls>2.0 and balls<3:
        print("Очень слабое")
    elif balls>=3.0 and balls<4:
        print("Слабое")
    elif balls>=4.0 and balls<5:
        print("Промежуточное")
    elif balls>=5.0 and balls<6:
        print("Умеренное")
    elif balls>=6.0 and balls<7:
        print("Сильное")
    elif balls>=7.0 and balls<8:
        print("Очень сильное")
    elif balls>=8.0 and balls<10:
        print("Огромное")
    elif balls>=10.0:
        print("Разрушительное")