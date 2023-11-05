#!/usr/bin/env python

import math

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Эта программа переводит человеческий возраст в собачий эквивалент.")
    human_age = float(input("Введите человеческий возраст в годах:"))
    dog_age = 0
    if (human_age <= 21):
        dog_age = human_age / 10.5
    elif (human_age > 21):
        dog_age = 2 + (human_age-21)/4
    print("Человеческий возраст %.2f лет равен собачьему %.2f лет" % (human_age,dog_age) )