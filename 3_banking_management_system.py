"                                                            🐍 Banking Management System 🐍                                                                                  "


import os
import csv

file_name = 'bank_data.csv'

# Ensure file exists before reading
if not os.path.exists(file_name):
    with open(file_name, 'w') as f:
        f.write("AccountNo,Name,Deposit,AccountType\n")  # Header

# Read data function
def read_file():
    with open(file_name, 'r') as file_obj:
        return [line.strip() for line in file_obj.readlines() if line.strip()]

class MyBank:
    def __init__(self):
        self.raw_data = read_file()

    def write_file(self):
        with open(file_name, 'w') as file_obj:
            file_obj.write("\n".join(self.raw_data) + "\n")

    def account_create(self):
        account_no = input('Enter the account number: ')
        name = input('Enter the account holder name: ')
        deposit = input('Enter the amount to deposit: ')
        account_type = input('Enter the account type (Savings/Current): ')

        data = f"{account_no},{name},{deposit},{account_type}"
        self.raw_data.append(data)
        self.write_file()
        print('Account created successfully!')

    def account_list(self):
        if len(self.raw_data) <= 1:
            print("No accounts found.")
            return

        print("\n".join(self.raw_data[1:]))  # Skip header
        print("*" * 40)

    def modify_account(self, account_no):
        for index, data in enumerate(self.raw_data):
            split_data = data.split(',')
            if split_data[0] == account_no:
                name = input("Enter new account holder name: ")
                deposit = input("Enter new deposit amount: ")
                acc_type = input("Enter new account type (S/C): ")

                self.raw_data[index] = f"{account_no},{name},{deposit},{acc_type}"
                self.write_file()
                print('Account updated successfully!')
                return
        print('Account not found!')

    def deposit_amount(self, account_no):
        amount = float(input('Enter the amount to deposit: '))
        for index, data in enumerate(self.raw_data):
            split_data = data.split(',')
            if split_data[0] == account_no:
                split_data[2] = str(float(split_data[2]) + amount)
                self.raw_data[index] = ",".join(split_data)
                self.write_file()
                print('Amount deposited successfully!')
                return
        print("Account not found!")

    def withdraw_amount(self, account_no):
        amount = float(input('Enter the amount to withdraw: '))
        for index, data in enumerate(self.raw_data):
            split_data = data.split(',')
            if split_data[0] == account_no:
                if float(split_data[2]) >= amount:
                    split_data[2] = str(float(split_data[2]) - amount)
                    self.raw_data[index] = ",".join(split_data)
                    self.write_file()
                    print('Amount withdrawn successfully!')
                else:
                    print("Insufficient balance!")
                return
        print("Account not found!")

    def delete_account(self, account_no):
        for index, data in enumerate(self.raw_data):
            if data.startswith(account_no + ","):
                del self.raw_data[index]
                self.write_file()
                print('Account deleted successfully!')
                return
        print('Account not found!')

    def search_account(self, account_no):
        return any(data.startswith(account_no + ",") for data in self.raw_data)

# Main program loop
bank = MyBank()

while True:
    print('''
        Welcome to the bank management system!
        
        1. Create Account
        2. Account List
        3. Modify Account
        4. Deposit Amount
        5. Withdraw Amount
        6. Delete Account
        7. Exit
    ''')

    try:
        choice = int(input('Enter your choice: '))
    except ValueError:
        print('Invalid choice! Please enter an integer value.')
        continue

    if choice == 1:
        bank.account_create()

    elif choice == 2:
        bank.account_list()

    elif choice == 3:
        num = input('Enter the account number for modification: ')
        if bank.search_account(num):
            bank.modify_account(num)
        else:
            print('Account not found!')

    elif choice == 4:
        num = input('Enter the account number for deposit: ')
        if bank.search_account(num):
            bank.deposit_amount(num)
        else:
            print('Account not found!')

    elif choice == 5:
        num = input('Enter the account number for withdrawal: ')
        if bank.search_account(num):
            bank.withdraw_amount(num)
        else:
            print('Account not found!')

    elif choice == 6:
        num = input('Enter the account number for deletion: ')
        if bank.search_account(num):
            bank.delete_account(num)
        else:
            print('Account not found!')

    elif choice == 7:
        print("Thank you for using the bank management system!")
        break

    else:
        print('Invalid choice! Please enter a valid option.')
