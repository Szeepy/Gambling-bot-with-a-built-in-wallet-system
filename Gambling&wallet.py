import random

def deposit(balance, wallet):
    while True:
        try:
            amount = float(input("Enter amount to deposit: $"))
            if amount > 0:
                if amount <= wallet:
                    balance += amount
                    wallet -= amount
                    print(f"Deposited: ${amount:.2f}. New Bank Balance: ${balance:.2f}. Wallet: ${wallet:.2f}")
                    break
                else:
                    print("Insufficient funds in wallet.")
            else:
                print("Deposit amount must be positive.")
        except ValueError:
            print("Invalid amount entered. Please enter a number.")
    return balance, wallet

def withdraw(balance, wallet):
    while True:
        try:
            amount = float(input("Enter amount to withdraw: $"))
            if 0 < amount <= balance:
                balance -= amount
                wallet += amount
                print(f"Withdrew: ${amount:.2f}. New Bank Balance: ${balance:.2f}. Wallet: ${wallet:.2f}")
                break
            elif amount > balance:
                print("Insufficient funds in bank.")
            else:
                print("Withdrawal amount must be positive.")
        except ValueError:
            print("Invalid amount entered. Please enter a number.")
    return balance, wallet

def check_balance(balance, wallet):
    print(f"Bank Balance: ${balance:.2f}")
    print(f"Wallet: ${wallet:.2f}")

def gamble(wallet):
    while True:
        try:
            bet = float(input("Enter amount to bet: $"))
            if bet > 0:
                if bet <= wallet:
                    outcome = random.choice([True, False])  # 50% chance to win or lose
                    if outcome:
                        wallet += bet
                        print(f"You won ${bet:.2f}! New Wallet Balance: ${wallet:.2f}")
                    else:
                        wallet -= bet
                        print(f"You lost ${bet:.2f}. New Wallet Balance: ${wallet:.2f}")
                    break
                else:
                    print("Insufficient funds in wallet.")
            else:
                print("Bet amount must be positive.")
        except ValueError:
            print("Invalid amount entered. Please enter a number.")
    return wallet
    

        
    
    
#--made by Szeepy on github--#





def main():
    balance = 100.0  # Initial bank balance
    wallet = 50.0    # Initial wallet balance
    while True:
        print("\n--- Bank Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Gamble")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()
        if choice == '1':
            balance, wallet = deposit(balance, wallet)
        elif choice == '2':
            balance, wallet = withdraw(balance, wallet)
        elif choice == '3':
            check_balance(balance, wallet)
        elif choice == '4':
            wallet = gamble(wallet)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()