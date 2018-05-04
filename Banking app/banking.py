#!/usr/bin/env python

from models import BankAccount

accounts = {}

def main():
    while True:
        option = input("Which option do you want to run (M for menu)?\n>")
        if option == "M":
            print("""
            Press 1 to create an account
            Press 2 to close an account
            Press 3 to make a deposit
            Press 4 to make a withdrawal
            Press 5 to make a transfer
            Press 6 to list all open accounts
            Press Q to leave this program""")
        elif option == "1":
            account_type = input("For checking, press C. For Savings, press S.\n>")
            if account_type == "C" or "c":
                nickname = input("What's the account nickname?\n>")
                balance = int(input("What's the opening balance?\n>"))
                new_account = BankAccount("Checking", nickname, balance)
                accounts[nickname] = {"Checking"}
                print(new_account)
            elif account_type == "S" or "s":
                nickname = input("What's the account nickname?\n>")
                balance = int(input("What's the opening balance?\n>"))
                new_account = BankAccount("Savings", nickname, balance)
                print(new_account)
        elif option == "3":
            amount = int(input("How much do you want to deposit on your account?\n>"))
            new_account.deposit(amount)
            print(new_account)
        elif option == "4":
            amount = int(input("How much do you want to withdraw from your account?\n>"))
            new_account.withdraw(amount)
            print(new_account)
        elif option == "Q" or "q":
            break

if __name__ == "__main__":
    # execute only if run as a script
    main()
