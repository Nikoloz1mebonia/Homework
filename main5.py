# N1
class Currency:
    def __init__(self, value, unit="GEL"):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value}.00 {self.unit}"

    def changeTo(self, unitname):
        if self.unit == "gel" or self.unit == "GEL":
            if unitname == "USD" or unitname == "usd":
                return self.value / 3, unitname
            elif unitname == "eur" or unitname == "EUR":
                return self.value / 2.7, unitname
            else:
                return "invalid currency"
        elif self.unit == "USD" or self.unit == "usd":
            if unitname == "GEL" or unitname == "gel":
                return self.value * 2.55
            elif unitname == "eur" or unitname == "EUR":
                return self.value * 0.92
            else:
                return "invalid currency"
        elif self.unit == "EUR" or self.unit == "eur":
            if unitname == "GEL" or unitname == "gel":
                return self.value * 2.77
            elif unitname == "usd" or unitname == "USD":
                return self.value * 1.08
            else:
                return "invalid currency"
        else:
            return "invalid currency"

    def __add__(self, other):
        if self.unit == other.unit:
            return f"{self.value + other.value} {self.unit}"
        elif self.unit != other.unit:
            x = other.changeTo(self.unit)
            return f"{self.value + x} {self.unit}"
        else:
            print("error")

    def __mul__(self, other):
        if other is int(other) or other is float(other):
            return f"{self.value * other} {self.unit}"
        else:
            return TypeError("გამრავლების ოპერაცია უნდა შესრულდეს მხოლოდ მთელ ან ათწილად რიცხვზე.")

    def __rmul__(self, other):
        if other is int(other) or other is float(other):
            return f"{self.value * other} {self.unit}"
        else:
            return TypeError("გამრავლების ოპერაცია უნდა შესრულდეს მხოლოდ მთელ ან ათწილად რიცხვზე.")

    def __gt__(self, other):
        other.value = other.changeTo(self.unit)
        if self.value > other.value:
            return f"{self.value} > {other.value}"
        elif self.value < other.value:
            return f"{self.value} < {other.value}"
        else:
            return f"{self.value} = {other.value}"


obj1 = Currency(200, "eur")
obj2 = Currency(120, "usd")
print(obj1)
print(obj1.changeTo("gel"))
print(obj1 + obj2)
print(obj1 * 3)
print(3 * obj2)
print(obj1.__gt__(obj2))
# N2
class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"name:{self.name}, deposit:{self.deposit}, loan: {self.loan}"


class House:
    def __init__(self, id, price, owner, status="გასაყიდი"):
        self.id = id
        self.price = price
        self.status = status
        self.owner = Person(owner)

    def sell_house(self, buyer, amount=None):
        if amount is None:
            self.owner.deposit += self.price
            self.owner = buyer
            self.status = "გაყიდული"
            print(f"new owner:{buyer.name}, status: {self.status}, id: {self.id}")
        else:
            self.owner.deposit += self.price
            self.owner.loan += amount
            self.owner = buyer
            self.status = "გაყიდულია სესხით"
            print(f"new owner:{buyer.name}, deposit: {buyer.deposit}, status: {self.status}, new owners loan:"
                  f" {self.owner.loan}")


owner = Person("nini")
buyer = Person("nika", 5000)
h1 = House(123, 30000, owner)
h1.sell_house(buyer)
h1.sell_house(buyer, h1.price)
print(owner)
print(buyer)
# N3
class Plane:
    def __init__(self):
        print("this is plane class")

    def move(self):
        print("plane can fly")

    def speed(self):
        print("its speed is up to 400 km/h")


class Bus:
    def __init__(self):
        print("this is bus class")

    def move(self):
        print("bus can move on roads")

    def speed(self):
        print("its speed is up to 80km/h")


pl1 = Plane()
bus1 = Bus()
bus1.move()
bus1.speed()
pl1.move()
pl1.speed()


def movement(argument):
    argument.speed()
    argument.move()


movement(pl1)
movement(bus1)
