# 
class BankAccount:

    # - Class Attributes
    bank_name = "BIAT"
    all_accounts = []
    # id
    account_default_id = 0
    #Constructor
    def __init__(self, balance = 0, int_rate = 0.025):
        # Instance Attribute
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.account_default_id += 1
        self._id = BankAccount.account_default_id
        BankAccount.all_accounts.append(self)    

    # Methods  
    # - Instance Method
    def deposit(self, amount):
        self.balance += amount
        return self
    
    # - Instance Method
    def withdraw(self, amount):
        self.balance -= amount
        return self

    @classmethod
    def get_account(cls,id):
        return cls.all_accounts[id-1]

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name
    
    @classmethod
    def all_balances(cls):
        total = 0
        for account in cls.all_accounts:
            if account.bank_name == "BIAT":
                total += account.balance 
        return total

    @staticmethod
    def check_withdraw(balance,amount):
        if balance > amount:
            return True
        else:
            return False
