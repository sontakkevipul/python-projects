balance = 10000
pin = "1234"

print("===== ATM MANAGEMENT =====")

entered_pin = input("Enter your PIN: ")

if entered_pin == pin:

    while True:

        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Current Balance:", balance)

        elif choice == "2":
            amount = int(input("Enter amount to deposit: "))

            if amount > 0:
                balance = balance + amount
                print("Amount deposited successfully")
                print("Current Balance:", balance)
            else:
                print("Enter a valid amount")

        elif choice == "3":
            amount = int(input("Enter amount to withdraw: "))

            if amount <= 0:
                print("Enter a valid amount")

            elif amount <= balance:
                balance = balance - amount
                print("Please collect your cash")
                print("Current Balance:", balance)

            else:
                print("Insufficient balance")

        elif choice == "4":
            print("Thank you for using ATM")
            break

        else:
            print("Invalid choice")

else:
    print("Incorrect PIN")
