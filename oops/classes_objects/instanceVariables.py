class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


circle = Circle(5)
print(f"Area of the circle: {circle.area()}")  # Output: Area of the circle: 78.5
