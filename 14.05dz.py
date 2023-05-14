#3
class Car:
    def __init__(self , brand , model , year):
        self.brand = brand
        self.model = model
        self.year = year
    def finish(self):
        return (f"Марка: {self.brand} "
                f"\nМодель: {self.model} "
                f"\nРік: {self.year}")
result = Car("Mazda" , "CX-30" , 2022)
print(result.finish())