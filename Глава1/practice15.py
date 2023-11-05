#!/usr/bin/env python


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Эта программа конвертирует длинну из футов в другие единицы.")
    feet = float(input("Введите длинну футах: "))
    inches = feet * 12
    yard = feet / 3
    mile = feet / 5280
    print("В дюймах это будет: %.4f" % (inches) )
    print("В ярдах это будет: %.4f" % (yard) )
    print("В милях это будет: %.4f" % (mile) )