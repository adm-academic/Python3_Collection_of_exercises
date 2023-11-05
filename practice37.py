#!/usr/bin/env python

import math

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Эта прогамма определяет какая введена буква латинского алфавита, гласная или согласная.")
    vstr = str(input("Введите букву латинского алфаита:"))
    letter = vstr[0]
    if letter in ['a','e','i','o','u']:
        print("Введена гласная буква %s" % letter)
    elif letter == 'y':
        print("Введена буква y, она может быть и гласной и согласной")
    else:
        print("Введена согласная буква %s " % letter)