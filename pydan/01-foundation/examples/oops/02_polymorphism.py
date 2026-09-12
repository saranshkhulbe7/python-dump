class Car:
    total_cars = 0

    def __init__(self, brand, model) -> None:
        self.__brand = brand
        self.__model = model
        Car.total_cars += 1

    def fuel_type(self):
        return "Petrol and Diesel"

    @classmethod
    def general_description(self):
        print(self.total_cars)


maruti = Car("Maruti", "M124")
sedan = Car("Maruti", "M124")

maruti.general_description()
sedan.general_description()
Car.general_description()
