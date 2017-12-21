#!/usr/bin/env python

from banking_app.models import BankAccount


def main():
    # while True:
    print("To make an account, use option 1.")
    option = input("Which option do you want to run?\n")
    if option == "1":
        account_type = input("For checking, press C. For Savings, press S.\n")
        if account_type == "C":
            new_account = BankAccount("Checking")
            print(new_account)

if __name__ == "__main__":
    # execute only if run as a script
    main()
