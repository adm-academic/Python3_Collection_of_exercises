#!/usr/bin/env python

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Эта прогамма переводит американский расход топлива в канадский.")
    print("Американский расход топлива измеряется в 'Миллях на Галлон'")
    print("Канадский расход топлива измеяется в 'Литрах на 100 КМ'")
    # 1 Миля на галлон эквивалентно 235,22 Литров на 100 километров
    mpg=float( input("Введите расход топлива в американском стиле(миллях на галлон):") )
    lpk = 235.215 / mpg
    print("Указанный американский расход топлива равен следующему канадскому: %.4f" % \
          (lpk) )