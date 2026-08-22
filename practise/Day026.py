class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        return self.balance

# Example usage:
account = BankAccount("6387379690", "Harsh Singh", 1280000)
print(f"Account Holder: {account.account_holder}")
print(f"Account Number: {account.account_number}")
print(f"Balance: {account.get_balance()}")
account.deposit(6400)
print(f"Balance after deposit: {account.get_balance()}")
account.withdraw(5000)
print(f"Balance after withdrawal: {account.get_balance()}")