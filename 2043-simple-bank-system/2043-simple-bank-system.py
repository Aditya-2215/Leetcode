class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        self.n = len(balance)

    def isValid(self, account):
        return 1 <= account <= self.n

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if (not self.isValid(account1) or
            not self.isValid(account2) or
            self.balance[account1 - 1] < money):
            return False

        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self.isValid(account):
            return False

        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if (not self.isValid(account) or
            self.balance[account - 1] < money):
            return False

        self.balance[account - 1] -= money
        return True