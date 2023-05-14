#2
class Rectangle:
    def __init__(self , width, height):
        self.width = width
        self.height = height
    def perimeter(self):
        return (self.width + self.height) * 2
    def area(self):
        return self.width * self.height
rezult = Rectangle(10, 5)
print("Периметр:", rezult.perimeter())
print("Площа:", rezult.area())
