class MyClass:
    x = 100


p1 = MyClass()
print(p1.x)
print(p1)


class ThisClass:
    def myfunc(self):
        print("hello mate")


obj = ThisClass()
obj.myfunc()

# Instance Method Use Case
# When methods need to interact with instance attributes, like modifying the state of an object.


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance

account = BankAccount()
print(account.deposit(100))  # Output: 100
print(account.withdraw(50))  # Output: 50
print(account.withdraw(100))  # Output: Insufficient funds

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

# Creating an instance of the Dog OOPS
my_dog = Dog("Buddy", 3)

# Calling instance methods
print(my_dog.bark())        # Output: Buddy says woof!
print(my_dog.get_age())     # Output: 3
my_dog.set_age(4)
print(my_dog.get_age())     # Output: 4


class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y


# Calling static methods
print(MathOperations.add(5, 3))       # Output: 8
print(MathOperations.subtract(5, 3))  # Output: 2



# Instance Methods: Have access to the instance (self) and can access and modify instance attributes.
# Static Methods: Do not have access to the instance or OOPS (self or cls). They operate independently of OOPS or instance data.


class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5 / 9


print(TemperatureConverter.celsius_to_fahrenheit(0))  # Output: 32.0
print(TemperatureConverter.fahrenheit_to_celsius(32))  # Output: 0.0

# global, class, local variables

i, j = 15, 20  # i j are global variable
class NewClass:
    a, b = 10, 20  # a b are class Variables

    def add(self, x, y):   # x y are local variables
        print(f'{x+y} are local variables and can be directly accessed ')
        print(f'{self.a + self.b} are class variables use self to access them')
        print(i, j, "global variables")


print(NewClass().add(100, 200))

# global, class, local variables with same name

a, b = 15, 20
class SameClass:
    a, b = 10, 20

    def add(self, a, b):
        print(a, b) # local variables
        print(self.a, self.b) # class variables
        print(globals()['a'], globals()['b']) # global variables


print(SameClass().add(2, 3))


# constructor vs methods
class Person:
    name = "Rashmi"  # class variable

    def __init__(self, name, age):
        print(name)        # local variable (parameter passed to __init__)
        print(self.name)   # class variable (before reassignment)
        self.name = name   # instance variable (reassigned to the local variable 'name')
        # self.age = age   #  assign the age instance variable

    def myfunc(self):
        print("My name is", self.name)  # prints the instance variable 'self.name'


# Example usage:
p1 = Person("Ramya", 26)   # Object instance
p1.myfunc()


# Example Emp - constructor - eid, ename, sal => display ()

class Emp:
    def __init__(self, eid, ename, sal):
        # we can create class variable inside constructor as well as inside methods
        self.eid = eid
        self.ename = ename
        self.sal = sal

    def __str__(self):    # go with display method instead of str constructor as it only returns str data
        return f"{self.eid}, {self.ename}, {self.sal}"

    # def display(self):
    #     print(self.eid, self.ename, self.sal)


emp1 = Emp(780941, "Ramya", 3.8)
# emp1.display()
print(emp1)

class Student(Person):
    pass

