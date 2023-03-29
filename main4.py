# N1
class People:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def get_email(self):
        return f"your email is {self.firstname}.{self.lastname}.school@edu.ge"


class Lecturer(People):
    def __init__(self, firstname, lastname, salary):
        super().__init__(firstname, lastname)
        self.salary = salary

    def get_email(self):
        return f"your email is {self.firstname}.{self.lastname}@edu.ge"


class Student(People):
    def __init__(self, firstname, lastname, courses):
        super().__init__(firstname, lastname)
        self.courses = list(courses)

    def get_email(self):
        return f"your email is {self.firstname}.{self.lastname}.1@edu.ge"


person1 = People("Nikoloz", "Mebonia")
print(person1.get_email())
person2 = Student("Anastasia", "Maisuradze", ["math", "english", "history"])
print(person2.get_email())
print(person2.courses)
person3 = Lecturer("Nini", "kvinikaze", 30000)  # ბევრად მეტს გისურვებ!!!
print(person3.get_email())
print(person3.salary)


# N2
class Libraryitem:
    def __init__(self, title, subject, status):
        self.title = title
        self.subject = subject
        self.status = status

    def booking(self):
        if self.status == "available":
            self.status = "occupied"
            print("the item has been booked")
        elif self.status == "occupied":
            print("the item is occupied so it can't be booked")
        else:
            print("try again")


class Book(Libraryitem):
    def __init__(self, ISBN, authors, title, subject, status):
        super().__init__(title, subject, status)
        self.ISBN = ISBN
        self.authors = authors


class Magazine(Libraryitem):
    def __init__(self, journalname, volume, status, title=None, subject=None):
        super().__init__(title, subject, status)
        self.journalname = journalname
        self.volume = volume


class CD(Libraryitem):
    def __init__(self, title, status, subject=None):
        super().__init__(title, subject, status)

    def booking(self):
        print("the item can not be booked")


item1 = Libraryitem("book", "history", "occupied")
item1.booking()
print(item1.status)
item2 = CD("something", "available")
item2.booking()


# N3
class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __str__(self):
        return f"hello {self.firstname} {self.lastname}, age:{self.age}"


class Employee:
    def __init__(self, profession, monthly_salary, working_hours):
        self.profession = profession
        self.monthly_salary = monthly_salary
        self.working_hours = working_hours

    def hourly_salary(self):
        return (self.monthly_salary / 24) // self.working_hours


class Doctor(Person, Employee):
    def __init__(self, firstname, lastname, age, profession, monthly_salary, working_hours):
        Person.__init__(self, firstname, lastname, age)
        Employee.__init__(self, profession, monthly_salary, working_hours)

    def perform_operation(self):
        print("operation performed")


person4 = Doctor("nikolozi", "mebonia", 15, "doctor", 4000, 9)
print(person4.firstname, person4.lastname, person4.age, person4.profession, person4.monthly_salary,
      person4.working_hours)
print(person4)
person4.perform_operation()
print(person4.hourly_salary())
