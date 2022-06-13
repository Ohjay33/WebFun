class BankAccount:

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display_account_info(self):
        print(self.int_rate)
        print(self.balance)


    def print_instances(cls):
        for i in cls.all_instances:
            print(i.display_account_info())

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        else:
            print('Your account balance is negative!')

ohjay = BankAccount(0.2, 0)
sue = BankAccount(0.2, 0)

ohjay.deposit(100)
ohjay.deposit(500)
ohjay.deposit(500)
sue.deposit(1000)
sue.deposit(1000)
sue.deposit(1000)
sue.withdraw(500)
sue.yield_interest()
print(sue.balance)
print(ohjay.balance)
print(ohjay.int_rate)
print(ohjay.yield_interest())





# @classmethod
# def print_instances(cls):
#     for i in cls.all_instances:
#         print(i.display_account_info())



