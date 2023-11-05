#!/usr/bin/env python

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("*** Вы сдаёте в приёмку бутылки.***\n"+
          "Бутылки объемом 1 литр и меньше стоят $0,10\n"+
          "а бутылки большего объема – $0,25")
    print("Введите сколько бутылок каждого объёма вы готовы сдать в пункт приёмки:")
    less_and_liter = float(input("Менее литра и литр:"))
    more_than_liter = float(input("Более литра:"))
    summa_less_and_liter = less_and_liter * 0.10
    summa_more_than_liter = more_than_liter * 0.25
    summa_all = summa_less_and_liter + summa_more_than_liter
    print( "Сумма за все бутылки: $%.2f" % summa_all )