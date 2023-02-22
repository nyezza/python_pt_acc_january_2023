# 
from bank_account import BankAccount
class User:
    def __init__(self, name,age, email):
        self.email = email
        self.name = name
        self.age = age
        self.bank_accounts = [BankAccount()] # Classes Association
        self.account_ids = []

    # def all_my_accounts(self):
    #     for account in BankAccount.all_accounts:
    #         if account.id in self.account_ids:
    #             print(account.balance)
# FIXME : 

john = User("John",39,"j@email.com")
# print("Bank Account Id",john.bank_accounts[0].id)
# alex = User("Alex", 35, "alex.email.com")
# john.bank_accounts.append(BankAccount(1000,0.5))
# john.bank_accounts.append(BankAccount(5000,0.5))
# john.bank_accounts.append(BankAccount(2000,0.5))
for account in john.bank_accounts:
    print(account.id,"----",account.balance, "----", account.bank_name)
BankAccount()
print(len(BankAccount.all_accounts))

# print(john.bank_accounts[0].all_balances())
# print(john.bank_accounts[0].check_withdraw(john.bank_accounts[1].balance, 2000))

# print(j)