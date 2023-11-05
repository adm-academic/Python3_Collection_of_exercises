#!/usr/bin/env python

import math

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Программа по номеру месяца определяет количество дней в нём")
    nmonth = int(input("введите номер месяца:"))
    if nmonth < 1 or nmonth > 12:
        print("такого месяца не существует")
    else:
        if nmonth in [1,3,5,7,8,10,12]:
            print("в месяце %d - 31 день" % nmonth )
        elif nmonth in [4,6,9,11]:
            print("в месяце %d - 30 дней" % nmonth)
        elif nmonth == 2:
            print("в %d месяце 28 или 29 дней" % nmonth)