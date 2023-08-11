class Account:
    def __init__(self, name):
        self.account_name = name
        self.account_balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.account_balance

    def get_name(self):
        return self.account_name


# Example usage
account = Account("John Doe")
print(account.get_name())  # Output: John Doe
print(account.get_balance())  # Output: 0

print(account.deposit(100))  # Output: Deposited 100 units. New balance: 100
print(account.withdraw(30))  # Output: Withdrew 30 units. New balance: 70
print(account.get_balance())  # Output: 70
