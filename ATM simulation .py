balance = 10000
while True :
    print("\n ATM menu")
    print("1. check balance")
    print("2. Deposite")
    print("3. Withdraw")
    print("4. Exit")
    
    choice =int(input("enter your choice"))
    
    if choice == 1:
        print(f"Your current balance is ₹{balance}")
    elif choice == 2:
        amount=int(input("enter amount to deposite"))
        balance += amount
        print(f"{amount} deposited successfully new balnace {balance}")
    elif choice == 3:
        amount = int(input("enter amount to withdraw"))
        if amount <= balance:
                balance -= amount
                print(f"{amount} withdraw successfully Remaining balance {balance}")
        
        else:
            print("insufficient balance")
    elif choice == 4:
        print("thank you for using our atm")
        break
    
    else:
        print("invalid choice please try again")
        