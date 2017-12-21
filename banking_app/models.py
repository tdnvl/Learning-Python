from random import randint


class BankAccount: # () not needed if we don't inherit
    def __init__(self, account_type, nickname="", balance=0):
        self.account_type = account_type
        self.nickname = nickname
        self.balance = balance
        n = 7
        self.account_number = ''.join(["%s" % randint(0, 9) for num in range(0, n)])

    def __str__(self):
        return "{}: {}".format(self.account_type,self.account_number)

    def withdraw(self,amount):
        self.balance -= amount

    def deposit(self,amount):
        self.balance += amount

    def transfer_to(self,account,amount):
        self.withdraw(amount)
        account.deposit(amount)

    def transfer_from(self,account,amount):
        account.withdraw(amount)
        self.deposit(amount)


