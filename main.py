class Person:
    def __init__(self, name, gender, age, income):
        self.name = name
        self.gender = gender.lower()
        self.age = age
        self.income = income

    def __str__(self):
        return f"name: {self.name}, gender: {self.gender}, age: {self.age}, income: {self.income}"

    def expense(self):
        x = (self.income * 20) / 100
        y = (self.income * 1) / 100
        return x + y

    def danazogi(self):
        if self.age < 30:
            if self.gender == "female":
                return f"danazogi: {30 * (self.income * 1) / 100}"
            elif self.gender == "male":
                return f"danazogi: {35 * (self.income * 1) / 100}"
            else:
                return "error"
        elif self.age == 30:
            if self.gender == "female":
                return f"danazogi: {30 * (self.income * 1) / 100}"
            elif self.gender == "male":
                return f"danazogi: {35 * (self.income * 1) / 100}"
            else:
                return "error"
        elif self.age > 30:
            if self.gender == "female":
                x = 60 - self.age
                return f"danazogi: {x * (self.income * 1) / 100}"
            elif self.gender == "male":
                x = 65 - self.age
                return f"danazogi: {x * (self.income * 1) / 100}"
            else:
                return "error"
        else:
            return "error"

    def year_amount(self):
        if self.gender == "male":
            gap = 65 - self.age
            return f"you have got {gap} years until pension"
        elif self.gender == "female":
            gap1 = 60 - self.age
            return f"you have got {gap1} years until pension"


p1 = Person("elene", "female", 36, 3000)
print(p1)
print(p1.expense())
print(p1.year_amount())
print(p1.danazogi())
