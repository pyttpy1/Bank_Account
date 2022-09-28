from mimetypes import init


class BankAccount:

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self
        
    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
        if amount > self.balance:
            self.balance -= 5
            print('not enough money charge a $5 fee')
        return self

    def display_account_info(self):
        print(f'Your balance is {self.balance} ')
        return self

    def yield_interest(self):
        self.balance = self.balance * (1 +self.int_rate)
        return self


mymoney = BankAccount(0.02,2000)
mymoney.withdraw(4000).display_account_info()
