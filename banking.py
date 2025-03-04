def show_balance():
    print(f"your balance is {balance}")


def deposit():
    amount = float(input("enter an amount to be deposited: "))

    if amount < 0:
        print("that not a valid amount")
        return 0
    else:
        return amount

def withdraw():
    amount = float(input("enter an withdraw amount: "))

    if amount > balance:
        print("insufficient amount")
        return 0
    elif amount < 0:
        print("must enter amount greater than zero")
        return 0
    else:
        return amount


balance = 0
is_running = True

while is_running:
    print("------------------")
    print("Banking programing")
    print("------------------")
    print("1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        show_balance()

    elif choice == '2':
        balance += deposit()

    elif choice == '3':
        balance -= withdraw()

    elif choice == '4':
        is_running = False

    else:
        print("this is not a valid choice")


