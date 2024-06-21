class Person:
    def __init__(self, name) -> None:
        # print(self.__dir__())
        self.name = name

    # override
    def __str__(self):
        return "Your name is: " + self.name

person1 = Person('A')
person2 = Person('B')
print(person1.__str__())
print(person1.__eq__(person2))