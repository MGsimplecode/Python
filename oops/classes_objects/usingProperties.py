class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return (self.celsius * 9/5) + 32


temp = Temperature(25)
print(f"{temp.celsius} Celsius is {temp.fahrenheit} Fahrenheit")  # Output: 25 Celsius is 77.0 Fahrenheit
