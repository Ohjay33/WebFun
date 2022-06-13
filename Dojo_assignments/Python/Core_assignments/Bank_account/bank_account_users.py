
class User:
    def __init__(self, name, email, type):
        self.name = name
        self.email = email
        self.type = type
        self.account = BankAccount(int_rate=0.05, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)

    def display_user_balance(self):
        print(self.name, self.account.balance, self.type)


    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)

        





# -----------NEW CLASS------------------//


class BankAccount:
    Bank_name = "wells Fargo"

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
        


    # def print_instances(cls):
    #     for i in cls.all_instances:
    #         print(i.display_account_info())

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        else:
            print('Your account balance is negative!')


ohjay = User("Oscar Moore", "oj@gmail", "checking")
sue = User("Suaddah Irvin", 'sue@yahoo.com', "savings")

ohjay.make_deposit(200)
ohjay.make_deposit(200)
ohjay.make_deposit(200)
sue.make_deposit(15000)
ohjay.transfer_money(sue,500)
sue.transfer_money(ohjay, 150)
ohjay.display_user_balance()
sue.display_user_balance()

