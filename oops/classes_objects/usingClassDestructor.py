class MyClass:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"{self.name} is deleted")


obj1 = MyClass("Object 1")
obj2 = MyClass("Object 2")

del obj1  # Output: Object 1 is deleted
# The object `obj2` will be deleted automatically when the script finishes execution
