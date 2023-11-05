#!/usr/bin/env python

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Интернет-магазин занимается продажей различных сувениров и")
    print("безделушек. Каждый сувенир весит 75 г, а безделушка – 112 г")
    s = int(input("Введите количество сувениров:"))
    b = int(input("Введите количество безделушек:"))
    massa_netto_gramm = float( (s*75) + (b*112) )
    massa_netto_kilogramm = massa_netto_gramm / 1000
    print("Итоговая масса посылки:(%.2f грамм), (%.2f килограмм)" %
          (massa_netto_gramm,massa_netto_kilogramm) )