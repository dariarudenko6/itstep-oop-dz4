#-----Завдання 2-----
import random

class Encoder:
    def __init__(self, number):
        self.__number = number

    def __encode(self):
        self.__number += random.randint(1, 10)

    def reveal(self):
        self.__encode()
        print(self.__number)
