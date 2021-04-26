while True: 

    bid_price = int(input('Введите стоимость автомобиля: '))
    year = int(input('Введите год выпуска автомобиля: '))
    engine = float(input('Введите объем двигателя автомобиля: '))


    print('Цена автомобиля покупки на аукционе:', '{}.00'.format(int(bid_price)))


    # Сбор аукциона
    def tax_auction(bid_price):

        if 0 <= bid_price <= 99.99:
            return 25
        elif 100 <= bid_price <= 299.99:
            return 50
        elif 300 <= bid_price <= 399.99:
            return 75
        elif 400 <= bid_price <= 499.99:
            return 125
        elif 500 <= bid_price <= 599.99:
            return 150
        elif 600 <= bid_price <= 799.99:
            return 175
        elif 800 <= bid_price <= 899.99:
            return 200
        elif 900 <= bid_price <= 999.99:
            return 225
        elif 1000 <= bid_price <= 1199.99:
            return 250
        elif 1200 <= bid_price <= 1399.99:
            return 275
        elif 1400 <= bid_price <= 1599.99:
            return 300
        elif 1600 <= bid_price <= 1699.99:
            return 325
        elif 1700 <= bid_price <= 1999.99:
            return 350
        elif 2000 <= bid_price <= 2499.99:
            return 425
        elif 2500 <= bid_price <= 2999.99:
            return 450
        elif 3000 <= bid_price <= 3499.99:
            return 500
        elif 3500 <= bid_price <= 4999.99:
            return 550
        elif 5000 <= bid_price <= 7499.99:
            return 625
        elif 7500 <= bid_price <= 7999.99:
            return 650
        elif 8000 <= bid_price <= 9999.99:
            return 700
        elif bid_price >= 10000:
            return bid_price * 0.07

    print('Сбор аукциона:', '{:>25}.00'.format(int(tax_auction(bid_price))))


    # Доставка
    def delivery(sea = 850, dry_land = 400, services = 200, brocker = 850):
        sum = sea + dry_land + services + brocker
        return sum

    print('Доставка:', '{:>31}.00'.format(int(delivery())))

    # Растаможка
    def customs_clearance(bid_price, engine = 3.0, year = 2021, dry_land = 400):

        base_tax = 61

        price_with_dry_land = bid_price + dry_land + int(tax_auction(bid_price))
        print(price_with_dry_land)


        # Пошлина
        duty = price_with_dry_land * 0.1
        print('Пошлина:', '{}.00'.format(int(duty)))

        # Акциз
        excise_tax = engine * base_tax if engine <= 3.0 else engine * (base_tax * 2)
        

        # Акциз с учетом года выпуска авто
        def year_tax():
            if engine <= 3:
                if year >= 2019:
                    return excise_tax
                elif year == 2018:
                    return excise_tax + base_tax * 2
                elif year == 2017:
                    return excise_tax + base_tax * 4
                elif year == 2016:
                    return excise_tax + base_tax * 6
                elif year == 2015:
                    return excise_tax + base_tax * 8
                elif year == 2014:
                    return excise_tax + base_tax * 10
                elif year == 2013:
                    return excise_tax + base_tax * 12
                elif year == 2012:
                    return excise_tax + base_tax * 14
                else:
                    return excise_tax + base_tax * 100
            else:
                if year >= 2019:
                    return excise_tax
                elif year == 2018:
                    return excise_tax * 2
                elif year == 2017:
                    return excise_tax * 3
                elif year == 2016:
                    return excise_tax * 4
                elif year == 2015:
                    return excise_tax * 5
                elif year == 2014:
                    return excise_tax * 6
                elif year == 2013:
                    return excise_tax * 7
                elif year == 2012:
                    return excise_tax * 8
        print('Акциз:', '{}.00'.format(int(year_tax())))
        

        # Пенсионный
        def pension_tax():
            price_with_taxs = price_with_dry_land + duty + year_tax()
            result = price_with_taxs * 0.03 if price_with_taxs < 13300 else price_with_taxs * 0.04
            return result

        print('Пенсионный:', '{}.00'.format(int(pension_tax())))


        def added_tax():
            result = (price_with_dry_land + duty + year_tax()) * 0.2
            return result

        print('НДС:', '{}.00'.format(int(added_tax())))

        total_tax = duty + year_tax() + added_tax()
        print('Итоговая растаможка:', '{:>20}.00'.format(int(total_tax)))
        return total_tax


    sertification = 213
    detailing = 150
    car_delivery = 200

    print('Сертификация:', '{:>26}.00'.format(int(sertification)))
    print('Детейлинг:', '{:>29}.00'.format(int(detailing)))
    print('Автовоз:', '{:>31}.00'.format(int(car_delivery)))


    total_car_price = bid_price + sertification + detailing + car_delivery + tax_auction(bid_price) + delivery() + customs_clearance(bid_price, engine, year)

    print('Итоговая стоимость автомобиля без ремонта:', '{:>20}.00'.format(int(total_car_price)))
