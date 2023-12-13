class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        return f"Driving {self.brand}"

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def info(self):
        return f"{self.brand} {self.model}"


car = Car("Toyota", "Corolla")
print(car.info())   # Output: "Toyota Corolla"
print(car.drive())  # Output: "Driving Toyota"
