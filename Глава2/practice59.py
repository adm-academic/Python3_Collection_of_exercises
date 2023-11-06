#!/usr/bin/env python

import math
import datetime

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Программа выводит дату следующую за указанной.")
    year = int(input("Введите год:"))
    month = int(input("Введите месяц:"))
    day = int(input("Введите день:"))
    dti = datetime.datetime(year,month,day)
    dtn = dti + + datetime.timedelta( days=1 )
    print( "Вы ввели дату ", dti.date(), " Следующая за ней дата ", dtn.date() )