# a simple ATM banking system where users can check their balance, deposit money, withdraw money, and exit the application.


balance = 15000
correct_pin = 1234

pin = int(input("Enter your ATM PIN: "))

if pin == correct_pin:

    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            print("Your Balance: ", balance)

        case 2:
            amount = int(input("Enter deposit amount: "))

            if amount > 0:
                balance += amount
                print("Deposit Successfull")
                print("Updated Balance:", balance)
            else:
                print("Invalid Amount")

        case 3:
            amount = int(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Invalid Amount")

            elif amount <= balance:
                balance -= amount
                print("Withdrawal Successful")
                print("Remaining Balance: ", balance)

            else:
                print("Insufficient Balance")

        case 4:
            print("Thank you for using our ATM")

        case _:
            print("Invalid Choice")

else:
    print("Incorrect PIN")