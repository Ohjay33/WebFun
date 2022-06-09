class User:
    def __init__(self, name, email, type):
        self.name = name
        self.email = email
        self.type = type
        

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(self.name, self.account_balance)


    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount


ohjay = User('Oscar Moore', "dojo.paid@gmail.com", 'checking')
sue = User('Suaddah Irvin', 'Sue@gmail.com', 'savings')
print(ohjay.name)
# ohjay.make_deposit(500)
# ohjay.make_deposit(500)
# ohjay.make_deposit(500)
# print(ohjay.account_balance)
print(ohjay.type)


