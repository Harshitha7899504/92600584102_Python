#8.Write a program to demonstrate encapsulation and abstraction using classes.

from abc import ABC, abstractmethod

# Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def show_balance(self):
        print("Balance:", self.__balance)


# Abstraction
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog barks")


# Demonstration
account = BankAccount(5000)
account.show_balance()

dog = Dog()
dog.sound()
