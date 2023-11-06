#!/usr/bin/env python

import math

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Эта прогамма определяет цвет по длинне волны света.")
    wave_lenth = float(input("Ведите длинну волны света в нанометрах: "))
    # Фиолетовый, Больше или равно 380 и меньше 450
    # Синий,  Больше или равно 450 и меньше 495
    # Зеленый, Больше или равно 495 и меньше 570
    # Желтый, Больше или равно 570 и меньше 590
    # Оранжевый, Больше или равно 590 и меньше 620
    # Красный, Больше или равно 620 и меньше или равно 750
    if wave_lenth<380 or wave_lenth>750:
        print("Введённая длинна волны находится за пределами видимой части спектра!")
        exit()
    if wave_lenth>=380 and wave_lenth<450:
        print("Фиолетовый")
    if wave_lenth>=450 and wave_lenth<495:
        print("Синий")
    if wave_lenth>=495 and wave_lenth<570:
        print("Зеленый")
    if wave_lenth>=570 and wave_lenth<590:
        print("Желтый")
    if wave_lenth>=590 and wave_lenth<620:
        print("Оранжевый")
    if wave_lenth>=690 and wave_lenth<=750:
        print("Красный")