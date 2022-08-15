class CarPrice:

    def __init__(self, bid_price, year, engine_value):
        self.base_tax = 52
        self.sertification = 213
        self.detailing = 150
        self.car_delivery = 200
        self.dry_land = 400
        self.delivery = 3000
        self.bid_price = int(bid_price)
        self.year = int(year)
        self.engine = float(engine_value)

    # Сбор аукциона
    def tax_auction(self):

        if 0 <= self.bid_price <= 99.99:
            return 25
        elif 100 <= self.bid_price <= 299.99:
            return 50
        elif 300 <= self.bid_price <= 399.99:
            return 75
        elif 400 <= self.bid_price <= 499.99:
            return 125
        elif 500 <= self.bid_price <= 599.99:
            return 150
        elif 600 <= self.bid_price <= 799.99:
            return 175
        elif 800 <= self.bid_price <= 899.99:
            return 200
        elif 900 <= self.bid_price <= 999.99:
            return 225
        elif 1000 <= self.bid_price <= 1199.99:
            return 250
        elif 1200 <= self.bid_price <= 1399.99:
            return 275
        elif 1400 <= self.bid_price <= 1599.99:
            return 300
        elif 1600 <= self.bid_price <= 1699.99:
            return 325
        elif 1700 <= self.bid_price <= 1999.99:
            return 350
        elif 2000 <= self.bid_price <= 2499.99:
            return 425
        elif 2500 <= self.bid_price <= 2999.99:
            return 450
        elif 3000 <= self.bid_price <= 3499.99:
            return 500
        elif 3500 <= self.bid_price <= 4999.99:
            return 550
        elif 5000 <= self.bid_price <= 7499.99:
            return 625
        elif 7500 <= self.bid_price <= 7999.99:
            return 650
        elif 8000 <= self.bid_price <= 9999.99:
            return 700
        elif self.bid_price >= 10000:
            return self.bid_price * 0.07

    # Растаможка
    def total_custom(self):
        duty = self.customs_clearance()[0]
        print('Пошлина:', '{}.00'.format(int(duty)))
        excise = self.year_tax()
        print('Акциз:', '{}.00'.format(int(excise)))
        pension = self.pension_tax()
        print('Пенсионный:', '{}.00'.format(int(pension)))
        percent_20_tax = self.added_tax()
        print('НДС:', '{}.00'.format(int(percent_20_tax)))
        total_tax = duty + excise + percent_20_tax + pension
        print('Итоговая растаможка:', '{}.00'.format(int(total_tax)))
        return total_tax

    # Пошлина
    def customs_clearance(self):
        price_with_dry_land = self.bid_price + self.dry_land + int(self.tax_auction())
        duty = price_with_dry_land * 0.1
        return duty, price_with_dry_land

    # Акциз с учетом года выпуска авто
    def year_tax(self):
        if self.engine <= 3.0:
            if self.year > 2021:
                return self.engine * self.base_tax * 1
            elif self.year == 2021:
                return self.engine * self.base_tax * 1
            elif self.year == 2020:
                return self.engine * self.base_tax * 2
            elif self.year == 2019:
                return self.engine * self.base_tax * 3
            elif self.year == 2018:
                return self.engine * self.base_tax * 4
            elif self.year == 2017:
                return self.engine * self.base_tax * 5
            elif self.year == 2016:
                return self.engine * self.base_tax * 6
            elif self.year == 2015:
                return self.engine * self.base_tax * 7
            else:
                return self.engine * self.base_tax * 15
        else:
            if self.year > 2021:
                return self.engine * (self.base_tax * 2) * 1
            elif self.year == 2021:
                return self.engine * (self.base_tax * 2) * 1
            elif self.year == 2020:
                return self.engine * (self.base_tax * 2) * 2
            elif self.year == 2019:
                return self.engine * (self.base_tax * 2) * 3
            elif self.year == 2018:
                return self.engine * (self.base_tax * 2) * 4
            elif self.year == 2017:
                return self.engine * (self.base_tax * 2) * 5
            elif self.year == 2016:
                return self.engine * (self.base_tax * 2) * 6
            elif self.year == 2015:
                return self.engine * (self.base_tax * 2) * 7

    # Пенсионный
    def pension_tax(self):
        duty, price_with_dry_land = self.customs_clearance()
        price_with_taxs = duty + price_with_dry_land + self.year_tax()
        result = price_with_taxs * 0.03 if price_with_taxs < 10000 else price_with_taxs * 0.04
        return result

    def added_tax(self):
        price_with_dry_land = self.customs_clearance()[1]
        result = (price_with_dry_land + self.year_tax()) * 0.2

        return result

    def get_final_price(self):
        total_car_price = self.bid_price + self.tax_auction() + self.dry_land + self.sertification + \
                          self.detailing + self.car_delivery + self.delivery + self.total_custom()
        print(total_car_price)

