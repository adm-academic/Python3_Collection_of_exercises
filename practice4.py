#!/usr/bin/env python

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Введите длинну и ширину садового участка в футах:")
    dlinna = float(input("Введите длинну участка в футах:"))
    shirina = float(input("Введите ширину комнаты в футах:"))
    ploshad_v_kvadratnyh_futah = dlinna*shirina
    ploshad_v_akrah = ploshad_v_kvadratnyh_futah / 43560
    print("Площадь садового участка равна: %f акров." % ploshad_v_akrah )