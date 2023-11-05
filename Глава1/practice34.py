#!/usr/bin/env python

import math

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Вычисляем стоимость вчерашнего хлеба")
    cena_hleba = 3.49
    skidka_na_vcherashnii_hleb = 0.60
    num = int(input("Введите количество вчерашних буханок хлеба: "))
    obycnaya_cena = num * cena_hleba
    skidka = obycnaya_cena * skidka_na_vcherashnii_hleb
    itogo = obycnaya_cena - skidka
    print("-----------------------------------------------")
    print("Обычная цена: %5.2f" % obycnaya_cena)
    print("Сумма скидки: %5.2f" % skidka)
    print("Итого: %12.2f" % itogo)
    print("-----------------------------------------------")