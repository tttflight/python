class Account:
    def __init__(self, name: str) -> None:
        self.account_name = name
        self.account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        This function increments the account balance by the specified amount
        :param amount: The amount to increment
        :return: Returns True or False boolean
        """
        if amount > 0:
            self.account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        This function decrements the account balance by the specified amount
        :param amount: The amount to decrement
        :return: Returns True or False boolean
        """
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        """
        This function gets the account balance
        :return: Account balance
        """
        return self.account_balance

    def get_name(self) -> str:
        """
        This functions gets the account name
        :return: Account name
        """
        return self.account_name


