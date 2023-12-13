class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

    @classmethod
    def multiply(cls, x, y):
        return x * y


print(MathOperations.add(5, 3))       # Output: 8
print(MathOperations.multiply(2, 4))  # Output: 8
