# program to create an instance of the bank account class and test the deposit and withdrawal functionality
import random

class BankAccount:
    def __init__(self, account_holder, initial_balance=0.0):
        self.__account_number = self.generate_account_number()
        self.__account_holder = account_holder
        self.__balance = initial_balance

    def generate_account_number(self):
        # Generate a random 10-digit account number
        return random.randint(1000000000, 9999999999)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}"
        elif amount > self.__balance:
            return "Insufficient funds."
        else:
            return "Invalid withdrawal amount."

    def display_balance(self):
        return f"Account Holder: {self.__account_holder}\nAccount Number: {self.__account_number}\nBalance: ${self.__balance:.2f}"


# Example usage:
if __name__ == "__main__":
    account1 = BankAccount("John Doe", 1000.0)
    print(account1.display_balance())
    print(account1.deposit(500.0))
    print(account1.withdraw(200.0))
    print(account1.display_balance())
