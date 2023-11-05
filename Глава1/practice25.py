#!/usr/bin/env python

import math

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Эта программа принимает на вход количество секунд и выводит их в фомате D:HH:MM:SS")
    seconds_in_day = 86400
    seconds_in_hour = 3600
    seconds_in_minute = 60
    seconds = int(input("Введите количество секунд: "))
    days = seconds / seconds_in_day
    seconds = seconds % seconds_in_day
    hours = seconds / seconds_in_hour
    seconds = seconds % seconds_in_hour
    minutes = seconds / seconds_in_minute
    seconds = seconds % seconds_in_minute
    print("Время в формате D:HH:MM:SS:", \
          "%d:%02d:%02d:%02d." % (days, hours, minutes, seconds))