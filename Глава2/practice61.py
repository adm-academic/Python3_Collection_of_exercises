#!/usr/bin/env python

from math import floor

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Определяем формат номерного знака. Всего допустимых формата два")
    print(" 1) 3 буквы и 3 цифры")
    print(" 2) 4 цифры 3 буквы")
    plate = input("Введите номерной знак машины: ")
    # Проверяем номерной знак. Необходимо проверить все 6 знаков для номера старого образца
    # и 7 знаков – для нового
    if len(plate) == 6 and \
            plate[0] >= "A" and plate[0] <= "Z" and \
            plate[1] >= "A" and plate[1] <= "Z" and \
            plate[2] >= "A" and plate[2] <= "Z" and \
            plate[3] >= "0" and plate[3] <= "9" and \
            plate[4] >= "0" and plate[4] <= "9" and \
            plate[5] >= "0" and plate[5] <= "9":
        print("Это номерной знак старого образца.")
    elif len(plate) == 7 and \
            plate[0] >= "0" and plate[0] <= "9" and \
            plate[1] >= "0" and plate[1] <= "9" and \
            plate[2] >= "0" and plate[2] <= "9" and \
            plate[3] >= "0" and plate[3] <= "9" and \
            plate[4] >= "A" and plate[4] <= "Z" and \
            plate[5] >= "A" and plate[5] <= "Z" and \
            plate[6] >= "A" and plate[6] <= "Z":
        print("Это номерной знак нового образца.")
    else:
        print("Неверный номерной знак.")