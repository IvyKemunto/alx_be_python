import os

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance_file = "account_balance.txt"
        if os.path.exists(self.balance_file):
            with open(self.balance_file, 'r') as file:
                self.account_balance = float(file.read().strip())
        else:
            self.account_balance = initial_balance
            self._save_balance()
    
    def _save_balance(self):
        with open(self.balance_file, 'w') as file:
            file.write(str(self.account_balance))
    
    def deposit(self, amount):
        self.account_balance += amount
        self._save_balance()
    
    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            self._save_balance()
            return True
        else:
            return False
    
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")
