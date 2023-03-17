# დავალება 1
class Rectangle:

    def __init__(self, width, length, color):
        self.width = width
        self.length = length
        self.color = color

    def perimeter(self):
        return 2 * (self.width + self.length)

    def area(self):
        return self.width * self.length


obj_1 = Rectangle(1, 5, "blue")
obj_2 = Rectangle(3, 3, "green")
obj_3 = Rectangle(3, 7, "purple")
print(obj_1.area())


# დავალება 2
class Car:

    def __init__(self, color, brand, model):
        self.color = color
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"მანქანის ბრენდი: {self.brand}, მანქანის მოდელი: {self.model}, მანქანის ფერი: {self.color}"


car_1 = Car("red", "ford", "mustang")
car_2 = Car("blue", "toyota", "prius")
car_3 = Car("green", "volkswagen", " golf")
print(car_1)
print(car_2)
print(car_3)


# დავალება 3
class Dog:
    def __init__(self, breed, size, age, color):
        self.breed = breed
        self.size = size
        self.age = age
        self.color = color

    def sleep(self):
        return "awww it fell asleep, isn't it cute?"

    def eat(self):
        return "niam niam, dog's love food"

    def sit(self):
        return "dog has sat, now give it a treat!!!"

    def run(self):
        return "dog ran a bunch and is tired, GIVE IT A TREAT IMMEDIATELY!!!!"


dog_1 = Dog("neapolian mastiff", "large", "5 years", "black")
dog_2 = Dog("maltese", "small", "2 years", "white")
dog_3 = Dog("chow chow", "medium", "3 years", "brown")
print(dog_3.sleep())
print(dog_3.sit())
print(dog_3.run())
print(dog_3.eat())
