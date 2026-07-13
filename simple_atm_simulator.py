
balance = 10000
correct_pin = 1234


def check_balance():
    print("Your current balance is:", balance)


def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print("Amount deposited successfully.")
    print("Updated balance =", balance)


def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))

    if amount <= balance:
        balance -= amount
        print("Please collect your cash.")
        print("Remaining balance =", balance)
    else:
        print("Insufficient balance!")


pin = int(input("Enter your 4-digit PIN: "))

if pin == correct_pin:

    while True:
        print("\n----- ATM MENU -----")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            check_balance()

        elif choice == 2:
            deposit()

        elif choice == 3:
            withdraw()

        elif choice == 4:
            print("Thank you for using the ATM.")
            break

        else:
            print("Invalid Choice!")

else:
    print("Incorrect PIN! Access Denied.")