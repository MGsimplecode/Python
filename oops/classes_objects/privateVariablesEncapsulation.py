class BankAccount:
    def __init__(self):
        self.__balance = 0  # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount()
account.deposit(100)
print(account.get_balance())  # Output: 100
# Trying to access private variable directly raises an AttributeError
# print(account.__balance)
