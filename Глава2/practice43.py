#!/usr/bin/env python

import math

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ##
    # Запрашиваем у пользователя частоту ноты и определяем ее название
    #
    print("Эта программа узнаёт ноту по частоте.")
    C4_FREQ = 261.63
    D4_FREQ = 293.66
    E4_FREQ = 329.63
    F4_FREQ = 349.23
    G4_FREQ = 392.00
    A4_FREQ = 440.00
    B4_FREQ = 493.88
    LIMIT = 1
    # Запрашиваем у пользователя частоту ноты
    freq = float(input("Введите частоту ноты (Гц): "))
    # Определяем ноту по частоте. Если нота не найдена, присваиваем переменной
    # пустую строку
    if freq >= C4_FREQ - LIMIT and freq <= C4_FREQ + LIMIT:
        note = "C4"
    elif freq >= D4_FREQ - LIMIT and freq <= D4_FREQ + LIMIT:
        note = "D4"
    elif freq >= E4_FREQ - LIMIT and freq <= E4_FREQ + LIMIT:
        note = "E4"
    elif freq >= F4_FREQ - LIMIT and freq <= F4_FREQ + LIMIT:
        note = "F4"
    elif freq >= G4_FREQ - LIMIT and freq <= G4_FREQ + LIMIT:
        note = "G4"
    elif freq >= A4_FREQ - LIMIT and freq <= A4_FREQ + LIMIT:
        note = "A4"
    elif freq >= B4_FREQ - LIMIT and freq <= B4_FREQ + LIMIT:
        note = "B4"
    else:
        note = ""
    # Отображаем результат или сообщение об ошибке
    if note == "":
        print("Ноты с заданной частотой не существует.")
    else:
        print("Введенная частота примерно соответствует ноте", note)