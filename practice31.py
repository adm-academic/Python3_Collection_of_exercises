#!/usr/bin/env python

import math

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Это конвертер единиц давления из киллопаскалей в другие единицы.")
    kpa = float(input("Введите давление  киллопаскалях:"))
    fkd = kpa / 6.895
    atm = kpa / 101.3
    mmrs = kpa * 7.501
    print("%.4f киллопаскалей будет равно %.4f фунтов на квадратный дюйм" % (kpa,fkd) )
    print("%.4f киллопаскалей будет равно %.4f атмосфер" % (kpa,atm) )
    print("%.4f киллопаскалей будет равно %.4f миллиметов ртутного столба" % (kpa,mmrs) )