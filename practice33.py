#!/usr/bin/env python

import math

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Программа сортиует 3 введённых числа.")
    a = float(input("Введи число 1:"))
    b = float(input("Введи число 2:"))
    c = float(input("Введи число 3:"))
    nums = [a,b,c]
    nums.sort()
    print("Числа в отсортированом виде: ", nums)