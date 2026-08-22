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

### I want to create a new class for My Bike###
class Bike:
    def __init__(self,brand,name,Cc,price):
        self.brand=brand
        self.name=name
        self.Cc=Cc
        self.price=price
    # I will now create a method to display the details of my future bike##
    def detailsofmybike(self):
        print(f"Brand: {self.brand}")
        print(f"Name: {self.name}")
        print(f"Cc: {self.Cc}")
        print(f"Price: {self.price}")
### Craeting an object of my bike class and displaying the details of my future bike##
mybike=Bike("Royal Enfield","Gurella","450cc","3.23 Lakh")
mybike.detailsofmybike()
print(
    f"Brand: {mybike.brand}",
    f"Name: {mybike.name}",
    f"Cc: {mybike.Cc}",
    f"Price: {mybike.price}",
    "I will buy it in March 2027"
)
