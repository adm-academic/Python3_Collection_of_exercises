#!/usr/bin/env python


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Программа запрашивает рост человека  футах и дюймах и переводит их в сантиметры")
    feet = float( input("Укажите сколько футов в вашем росте:") )
    inches = float( input("Укажите сколько дюймов в вашем росте:") )
    santi_1 = inches * 2.54;
    santi_2 = feet * 12 * 2.54;
    itog = santi_1 + santi_2
    print("Ваш рост в сантиметрах равен: %.2f см." % itog )