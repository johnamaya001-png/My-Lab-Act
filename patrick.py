balance = 10000.00  

print("---- Patrick's Bank -----")

while True:
    print("\nMENU")
    print("1. Check your Balance")
    print("2. Withdraw")
    print("3. Exit ATM")  
    
    choice = input("\nEnter: ")

    if choice == "1":
        print("Your current balance is: PHP", format(balance, '.2f'))

    elif choice == "2":
        while True:
            try:
                amount = float(input("Enter amount to withdraw: PHP "))

                if amount <= 0:
                    print("Error! Amount cannot be lesser than 0!")

                elif amount > balance:
                    print("Insufficient Funds!")
                    print("Your current balance is only PHP", format(balance, '.2f'))
                    print("\nWould you like to try again?")
                    print("1. Re-enter balance amount")
                    print("2. Check Balance")
                    print("3. Exit")
                      
                    option = input("Enter option: ")

                    if option == "1":
                        continue
                    elif option == "2":
                        print("Current balance is: PHP", format(balance, '.2f'))   
                    elif option == "3":
                        print("\nThank you for using our ATM!")
                        print("---End of Program--")
                        exit()

                else:
                    balance = balance - amount
                    print("\nYou have withdrawn successfully!")
                    print("You withdrew: PHP", format(amount, '.2f'))
                    print("Remaining Balance: PHP", format(balance, '.2f'))
                    print("Thank you for withdrawing!")
                    break  

            except ValueError:
                print("Error: Invalid input! Please enter numbers only.")

    elif choice == "3":
        print("\nThank you for using our ATM!")
        print("---End of Program--")
        break

    else:
        print("Invalid choice! Please only either 1, 2, or 3 only.")