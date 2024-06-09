from pyfiglet import figlet_format
import os

def show_balance(balance):
    print(f'Your balance is ${balance:.2f}')

def deposit():
    amount = float(input('How much do you want to deposit? $ '))
    if amount < 0:
        print('Amount must be more than zero')
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input('How much will you be withdrawing today? $ '))
    if amount < 0:
        print('Amount must be more than zero')
        return 0
    elif amount > balance:
        print('Insufficient Funds')
        return 0
    else:
        return amount

def access_transfer(balance):
    acct_no = input('Enter Account Number: ')
    if len(acct_no) != 10:
        print('Enter a valid account number')
        return 0
    amount = float(input('Amount to be transferred: $ '))
    if amount > balance:
        print("Insufficient Funds")
        return 0
    else:
        print("Transfer Successful")
        return amount

def transfer(balance):
    bank_name = input('Is receiver\'s Bank Name Access Bank? (Y/N) ').upper()
    if bank_name == 'Y':
        return access_transfer(balance)
    else:
        bank_name = input('Bank Name: ').upper()
        if 'BANK' not in bank_name:
            print('Invalid bank name')
            return 0
        amount = float(input('Amount to be transferred: $ '))
        if amount > balance:
            print("Insufficient Funds")
            return 0
        else:
            acct_no = input('Account Number: ')
            if len(acct_no) != 10:
                print('Enter valid Account Number')
                return 0
            print("Transfer Successful")
            return amount

def main():
    print(figlet_format('Access Bank', font='standard'))
    balance = 0
    is_running = True

    while is_running:
       # os.system('cls' if os.name == 'nt' else 'clear')
       # print(figlet_format('Access Bank', font='standard'))
        print('1. Show Balance\n2. Deposit\n3. Withdraw\n4. Transfer\n5. Exit\n')
        print('*******************************************')
        os.system('cls' if os.name == 'nt' else 'clear')
        choice = input('What can we do for you today? (Enter 1 - 5) ')
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            balance -= transfer(balance)
        elif choice == '5':
            is_running = False
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
        
        if is_running:
            input("Press Enter to continue...")

    os.system('cls' if os.name == 'nt' else 'clear')
    print('Thank you for banking with us')

if __name__ == '__main__':
    main()
