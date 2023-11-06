#!/usr/bin/env python

import math

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Эта программа оценивает сотрудников при помощи рейтингов.")
    RAISE_FACTOR = 2400.00
    UNACCEPTABLE = 0
    ACCEPTABLE = 0.4
    MERITORIOUS = 0.6
    rating = float(input("Введите рейтинг: "))
    if rating == UNACCEPTABLE:
        performance = "низкий"
    elif rating == ACCEPTABLE:
        performance = "удовлетворительный"
    elif rating >= MERITORIOUS:
        performance = "высокий"
    else:
        performance = ""
    if performance == "":
        print("Введен ошибочный рейтинг.")
    else:
        print("Основываясь на введенном рейтинге, ваш уровень: %s." % \
              performance)
    print("Прибавка к зарплате составит: $%.2f." % \
          (rating * RAISE_FACTOR))
