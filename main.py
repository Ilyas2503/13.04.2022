class Human:
    default_name = "no name"
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = 0

    def info(self):
        print (f"name: {self.name}")
        print (f"age: {self.age}")
        print (f"money: {self.__money}")
        print (f"house: {self.__house}")

    @staticmethod
    def default_info():
        print(f"name : {Human.default_name} age: {Human.default_age}")

    def __make_deal(self, house, money):
        self.__house = house
        self.__money = money

    def earn_money(self, salary):
        self.__money += salary
        print (f"you earned {salary} money,"
               f" your total is{self.__money}")

    def buy_house(self, house=0, price=0, ):
        house_price = house.final_price(price)
        if self.__money >= house_price:
            self.__make_deal(house, house_price)
            print ("you bough house")
        else:
            print ("Money is not enough")


class House:
    def __init__(self, area, price):
        self._area = area
        self.price = price

    def final_price(self, discount):
        final_price = round(self.price * (100 - discount) / 100, 2)
        print(f"price with discount {final_price}")
        return  final_price


class SmallHouse(House):
    default_area = 40

    def __init__(self, price):
        super(SmallHouse, self).__init__(SmallHouse.default_area,price)

Ilyas = Human("Ильяс",30)
Ilyas.info()
Ilyas.default_info()
Ilyas.earn_money(10000)
Ilyas.info()
house = House(100, 100000)
smallHouse = SmallHouse(50000)
Ilyas.info()
Ilyas.earn_money(50000)
Ilyas.info()
Ilyas.buy_house(smallHouse, 10)
print ("Ilyas and ilon mask are best friends")
Ilyas.earn_money(100000)
Ilyas.buy_house(house,20)
Ilyas.info()