#!/usr/bin/env python

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Вычислить количество энергии, требуемое для нагрева воды, а также стоимость нагрева")
    # Определим константы для удельной теплоемкости воды и стоимости электричества
    WATER_HEAT_CAPACITY = 4.186
    ELECTRICITY_PRICE = 8.9
    J_TO_KWH = 2.777e-7
    print("Введите объем воды и требуемое изменение температуры")
    volume = float(input("Объем воды в миллилитрах: "))
    d_temp = float(input("Повышение температуры (в градусах Цельсия): "))
    q = volume * d_temp * WATER_HEAT_CAPACITY# Вычисляем количество энергии в джоулях
    print("Потребуется %d Дж энергии." % q)# Отображаем результат в джоулях
    kwh = q * J_TO_KWH # Вычисляем потебляемую мощность
    cost = kwh * ELECTRICITY_PRICE# Вычисляем стоимость
    print("Стоимость энергии: %.2f центов." % cost)# Отображаем стоимость