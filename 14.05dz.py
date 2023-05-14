#1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def is_adult(self):
        return self.age > 18
rezult1 = Person("Настя" , 16)
rezult2 = Person("Ната" , 19)
print("Настя:" , rezult1.is_adult())
print("Ната:" , rezult2.is_adult())