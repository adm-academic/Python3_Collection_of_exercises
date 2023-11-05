#!/usr/bin/env python

import math

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Введи временной промежуток в виде количества дней, часов, минут и секунд")
    days    = int( input("Введи дни:") )
    hours   = int( input("Введи часы:") )
    minutes = int( input("Введи минуты:") )
    seconds = int( input("Введи секунды:") )
    result = seconds + (minutes * 60) + (hours * 60 *60) + (days*60*60*24)
    print("В секундах  сумме это будет %d" % result)