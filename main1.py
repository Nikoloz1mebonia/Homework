# დავალება ერთი
class Celsius:
    def __init__(self, temperature):
        self.__temperature = temperature

    def get_temp(self):
        return self.__temperature

    def set_temp(self, new_temp):
        self.__temperature = new_temp

    def del_temp(self):
        del self.__temperature

    temp_property = property(get_temp, set_temp, del_temp)


cel1 = Celsius(23)
cel2 = Celsius(-23)
print(cel1.temp_property)
cel1.temp_property = 20
print(cel1.temp_property)
del cel1.temp_property
print(cel2.temp_property)
cel2.temp_property = -20
print(cel2.temp_property)
del cel2.temp_property


# დავალება 2
class Bank_account:
    def __init__(self, account_name, balance=0):
        self.__account_name = account_name
        self.__balance = balance

    def __str__(self):
        return f"გამარჯობა {self.__account_name}, თქვენ ანგარისშზე გაქვთ {self.__balance} ლარი"

    def get_name(self):
        return self.__account_name

    def set_name(self, new_name):
        self.__account_name = new_name

    def deposit(self, amount):
        self.__balance += amount
        print(f"თანხის შეტანა შესრულებულია, ამჟამად თქვენ ანგარიშზე გაქვთ {self.__balance} ლარი")

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print(f"თანხის გამოტანა შესრულებულია, ამჟამად თქვენ ანგარიშზე გაქვთ {self.__balance} ლარი")
        else:
            print("ოპერაცია ვე შესრულდა ანგარიშზე არასაკმარისი თანხის გამო")


bank_account = Bank_account("nikolozi", 125)
print(bank_account)
money = int(input("ჩაწერეთ თანხის რაოდენობა რომლის შეტანაც გუნდათ: "))
bank_account.deposit(money)

money1 = int(input("ჩაწერეთ ღანხის რაოდენობა რომლის გამოტანაც გსურთ: "))
bank_account.withdraw(money1)

# # ძააან ბევრი ვიწვალე ნინიი მაგრამ რო მინდოდა ისე არ გამოვიდა
# დავალება 3
from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        return sqrt(self.x ** 2 + self.y ** 2)


point1 = Point(3, 5)
point2 = Point(6, 9)
print(point1.distance())
print(point2.distance())


# bonus

class Fraction:
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom

    def __str__(self):
        return f"{self.top}/{self.bottom}"

    def inverse(self):
        return f"this fraction upside down is {self.bottom}/{self.top}"

    def __add__(self, other):
        n = (self.top * other.bottom) + (self.bottom * other.top)
        d = self.bottom * other.bottom
        return Fraction(n, d)


num = Fraction(3, 4)
print(num)
print(num.inverse())
num1 = Fraction(2, 8)
sum1 = num + num1
print(sum1)
