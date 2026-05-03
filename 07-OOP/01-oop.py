from random import choices
from string import ascii_uppercase, digits


class Car:
    def __init__(
        self, brand: str, model: str, color: str, year: int
    ):  # this is a constructor method
        self.brand = brand  # attributes below are comming from brand parameter
        self.model = model
        self.color = color
        self.year = year

        numbers = "".join(choices(digits, k=3))
        letters = "".join(choices(ascii_uppercase, k=4))

        self.plate = numbers + "-" + letters # attributes below are auto made inside de constructor.
        self.mileage = 0
    
    def travel(self, miles_run: int):
        self.mileage += miles_run
        print(f'{self.model} traveled {miles_run}')
        print(f'Actual mileage {self.mileage} miles')


fiat_uno = Car("Fiat", "Uno", "Red", 1118)
print(fiat_uno.brand, fiat_uno.model, fiat_uno.color, fiat_uno.plate)


fiat_uno.travel(10)
fiat_uno.travel(56)