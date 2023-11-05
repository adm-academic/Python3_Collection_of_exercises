#!/usr/bin/env python

import math

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Эта программа узнаёт частоту звука по переданной ноте.")
    C4_FREQ = 261.63
    D4_FREQ = 293.66
    E4_FREQ = 329.63
    F4_FREQ = 349.23
    G4_FREQ = 392.00
    A4_FREQ = 440.00
    B4_FREQ = 493.88
    name = input("Введите название ноты в виде буквы и цифры, например C4: ")# Запрашиваем у пользователя название ноты
    ### Сохраняем название ноты и номер октавы в разных переменных
    note = name[0]
    octave = int(name[1])
    ### Получаем частоту ноты четвертой октавы
    if note == "C":
        freq = C4_FREQ
    elif note == "D":
        freq = D4_FREQ
    elif note == "E":
        freq = E4_FREQ
    elif note == "F":
        freq = F4_FREQ
    elif note == "G":
        freq = G4_FREQ
    elif note == "A":
        freq = A4_FREQ
    elif note == "B":
        freq = B4_FREQ
    ### Адаптируем частоту к конкретной октаве
    freq = freq / 2 ** (4 - octave)
    ### Выводим результат
    print("Частота ноты", name, "равна", freq)