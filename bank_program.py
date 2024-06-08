
def show_balance(balance):
    print(f'You balance is ${balance:.2f}')


def deposit():
    amount = float(input('How much do you want to deposit ? '))

    if amount < 0:
        print('Amount must be more than zero')
        return 0
    else:
        return amount


def withdraw(balance):
    amount = float(input('How much will you be withdrawing today ? '))

    if amount < 0:
        print('Amount must be more than zero')
        return 0
    
    elif amount > balance:
        print('Insufficient Funds')
        return 0
    
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print('Welcome to Access Bank')

        print('1.    Show Balance\n2.    Deposit\n3.    Withdraw\n4.    Exit')

        choice = input('What can we do for you today? (Enter 1 - 4) ')

        if choice == '1':
            show_balance(balance)
        
        elif choice == '2':
            balance += deposit()

        elif choice == '3':
            balance -= withdraw(balance)

        else:
            is_running = False

    print('Thanks you for banking with us')

if __name__ == '__main__':
    main()