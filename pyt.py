

import sys

class Account:
    def _init_(self, account_number, name, initial_balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New Balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New Balance: ${self.balance}")

    def display_balance(self):
        print(f"Account: {self.account_number} | Name: {self.name} | Balance: ${self.balance}")

class Bank:
    def _init_(self):
        self.accounts = {}

    def create_account(self, account_number, name, initial_balance=0):
        if account_number in self.accounts:
            print("Account number already exists.")
        else:
            self.accounts[account_number] = Account(account_number, name, initial_balance)
            print(f"Account created successfully for {name} with balance ${initial_balance}.")

    def deposit_to_account(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.deposit(amount)
        else:
            print("Account not found.")

    def withdraw_from_account(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found.")

    def display_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            account.display_balance()
        else:
            print("Account not found.")

    def display_all_accounts(self):
        if not self.accounts:
            print("No accounts to display.")
        else:
            for account in self.accounts.values():
                account.display_balance()

def display_menu():
    print("\n--- Banking System Menu ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Display Account Balance")
    print("5. Display All Accounts")
    print("6. Exit")

def main():
    bank = Bank()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            account_number = input("Enter account number: ")
            name = input("Enter account holder name: ")
            initial_balance = float(input("Enter initial balance: "))
            bank.create_account(account_number, name, initial_balance)

        elif choice == '2':
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            bank.deposit_to_account(account_number, amount)

        elif choice == '3':
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            bank.withdraw_from_account(account_number, amount)

        elif choice == '4':
            account_number = input("Enter account number: ")
            bank.display_account(account_number)

        elif choice == '5':
            bank.display_all_accounts()

        elif choice == '6':
            print("Exiting the Banking System.")
            sys.exit()

        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()

