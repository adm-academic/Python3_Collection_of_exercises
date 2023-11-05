#!/usr/bin/env python

import math

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Эта программа предназначена для расчета скорости объекта во время его соприкосновения с землей")
    vi = 0 # начальная скорость равна нулю
    a = 9.8 # ускрение сободного падения равно 9.8
    d = float(input("Введите высоту, с которой отпущен объект:"))
    vf = math.sqrt(vi**2 + 2*a*d)
    print("Скорость при соприкосновении с поверхностью равна %.2f м/с " % vf )