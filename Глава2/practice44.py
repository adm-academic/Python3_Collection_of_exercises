#!/usr/bin/env python

import math

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    moneys = {
        1  : 'Джордж Вашингтон',
        2: 'Томас Джефферсон',
        5: 'Авраам Линкольн',
        10: 'Александр Гамильтон',
        20: 'Эндрю Джексон',
        50: 'Улисс Грант',
        100: 'Бенджамин Франклин'
    }
    print("Эта программа выводит имя американского президента по номиналу банкноты.")
    nominal = int(input("Введите номинал банкноты США: "))
    if not nominal in moneys:
        print("Номинала долларов США %d не существует! " %nominal )
    else:
        print("На банкноте США %d долларов изображён %s." % (nominal,moneys[nominal]))