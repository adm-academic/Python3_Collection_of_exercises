#!/usr/bin/env python

import math

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Эта прогамма классифициует электомагнитные волны по частоте.")
    frequency = float(input("Введите частоту волны в Гц:"))
    if frequency<3e9 :
        print("Радиоволны")
    elif frequency>3e9  and frequency<=3e12:
        print("Микроволны")
    elif frequency>3e12  and frequency<=4.3e14 :
        print("Инфракрасное излучение")
    elif frequency>4.3e14 and frequency<=7.5e14 :
        print("Видимое излучение")
    elif frequency>7.5e14 and frequency<=3e17 :
        print("Ультрафиолетовое излучение")
    elif frequency>3e17 and frequency<=3e19 :
        print("Рентгеновское излучение")
    elif frequency>3e19 :
        print("Гамма-излучение")