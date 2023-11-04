#!/usr/bin/env python

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    percents=float(4);
    print("Банк открывает счета по 4% годовых, начисляемых в конце года.")
    print("Введите сумму первоначалного депозита для рассчёта суммы на счету")
    print("в конце первого,второго и третьего годов.")
    summa_deposita = float( input("введите сумму первоначального депозита:") )

    year_1_percent = (summa_deposita / 100) * percents
    year_1_summa   = summa_deposita + year_1_percent
    print("первый год сумма: %s" % year_1_summa)

    year_2_percent = (year_1_summa / 100) * percents
    year_2_summa   = year_1_summa + year_2_percent
    print("второй год сумма: %s" % year_2_summa)

    year_3_percent = (year_2_summa / 100) * percents
    year_3_summa   = year_2_summa + year_3_percent
    print("третий год сумма: %s" % year_3_summa)

