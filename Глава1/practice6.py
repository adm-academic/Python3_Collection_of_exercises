#!/usr/bin/env python

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Введите сумму заказа в ресторане для дальнейшего рассчёта налога и чаевых.")
    summa_zakaza = float( input("Введите сумму заказа:") )
    nalog = 10;
    charvye = 18;
    summa_naloga = (summa_zakaza / 100) * nalog
    summa_chaevyh = (summa_zakaza / 100) * charvye
    itogo = summa_zakaza + summa_naloga + summa_chaevyh
    print("Schet:")
    print("summa_zakaza=%.2f" % summa_zakaza )
    print("summa_naloga=%.2f" % summa_naloga )
    print("summa_chaevyh=%.2f" % summa_chaevyh )
    print("itogo=%.2f" % itogo )