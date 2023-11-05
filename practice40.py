#!/usr/bin/env python

import math

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Программа вводит соответвие шуму в децибелах известным источникам шума")
    decibells = int(input("введите уровень шума в децибелах от 0 и выше:"))
    table = [   "Тихая комната",#40
                "Будильник",#70
                "Газовая газонокосилка",#106
                "Отбойный молоток", #130
            ]
    if decibells>0 and decibells<40:
        print("Это тише чем в тихой комнате")
    elif decibells==40:
        print("Это уровень тихой комнаты")
    elif decibells>40 and decibells<70:
        print("Это между тихой комнатой и будильником")
    elif decibells==70:
        print("Это уровень будильника")
    elif decibells>70 and decibells<106:
        print("Это между будильником и газовой газонокосилкой")
    elif decibells==106:
        print("Так громко шумит газовая газонокосилка")
    elif decibells>106 and decibells<130:
        print("Этот звук попадает между газовой газонокосилкой и отбойным молотком")
    elif decibells==130:
        print("Так громко шумит отбойный молоток")
    elif decibells>130:
        print("Этот шум даже сильнее чем отбойный молоток!")