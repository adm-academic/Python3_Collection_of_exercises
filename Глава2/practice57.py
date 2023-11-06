#!/usr/bin/env python

import math

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Эта программа выставляет счёт за сотовый телефон в соответствии с заданием №57.")
    TARIFF_IN_DOLLARS = 15.0
    TARIFF_CALL_MINUTES = 50
    TARIFF_SMS = 50
    ADDITIONAL_MINUTES_PRICE_DOLLARS = 0.25
    ADDITIONAL_SMS_PRICE_DOLLARS = 0.15
    TAX_911_DOLLARS = 0.44
    GENERAL_TAX_PERCENTS = 5

    minutes_spent = int(input("Введите количество израсходованных минут:"))
    sms_spent = int(input("Введите число отправленных SMS:"))
    itogo = TARIFF_IN_DOLLARS

    print("-------------------------------------------------")
    print("Базовая сумма тарификации = %.2f" % TARIFF_IN_DOLLARS)
    if minutes_spent > TARIFF_CALL_MINUTES:
        minutes_over_tariff = minutes_spent - TARIFF_CALL_MINUTES
        minutes_over_tariff_summ = minutes_over_tariff * ADDITIONAL_MINUTES_PRICE_DOLLARS
        print("Дополнительно потрачено минут %f на сумму = %.2f" %
                        (minutes_over_tariff,minutes_over_tariff_summ) )
        itogo += minutes_over_tariff_summ
    if sms_spent >  TARIFF_SMS:
        sms_over_tariff = sms_spent - TARIFF_SMS
        sms_over_tariff_summ = sms_over_tariff * ADDITIONAL_SMS_PRICE_DOLLARS
        print("Дополнительно потрачено SMS - %f на сумму = %.2f" %
                        (sms_over_tariff,sms_over_tariff_summ) )
        itogo += sms_over_tariff_summ
    print("Отчисления на работу службы 911 = %.2f" % TAX_911_DOLLARS )
    itogo += TAX_911_DOLLARS
    tax_summ = (itogo / 100) * GENERAL_TAX_PERCENTS
    print("Налог %.2f = %.2f" % (GENERAL_TAX_PERCENTS,tax_summ) )
    itogo += tax_summ
    print("Итого общая сумма к оплате = %.2f " % itogo )
    print("-------------------------------------------------")
