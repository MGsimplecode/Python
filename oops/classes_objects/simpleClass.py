class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says Woof!"


# Creating objects of Dog class
dog1 = Dog("Buddy")
dog2 = Dog("Max")

print(dog1.bark())  # Output: "Buddy says Woof!"
print(dog2.bark())  # Output: "Max says Woof!"
