class Car:
    def __init__(self, brand, model) -> None:
        self.__brand = brand
        self.model = model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size) -> None:
        super().__init__(brand, model)
        self.battery_size = battery_size


class NexonElectricCar(ElectricCar):
    def __init__(self, brand, model, battery_size, series) -> None:
        super().__init__(brand, model, battery_size)
        self.series = series

    def describe(self):
        return f"{long_dash}\nBrand: {self.__brand}\nModel: {self.model}\nBattery Size: {self.battery_size}\nSeries: {self.series}\n{long_dash}"

    def get_brand(self):
        pass


my_car = ElectricCar("Toyota", "Corolla", "1000MAH")


long_dash = "-" * 20

print(isinstance(my_car, Car))
print(isinstance(my_car, ElectricCar))
print(isinstance(my_car, NexonElectricCar))
