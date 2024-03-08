# Data Science project - SafeBank case study 
# Revamp SafeBank online banking interface by ensuring user-friendliness

import random as rd


# Function validating the name
def validation(name):
    for char in name:
        if not (("A" <= char and char <= "Z") or ("a" <= char and char <= "z") or (char == " ")):
            return False
    return True

# Function generating balance
def check_bal():

    current_balance = rd.randint(100, 999999)
    return current_balance
balance_current = check_bal() # The program generates a random account balance


print("Welcome to SafeBank Banking App!\nPlease enter your details below : ")

account_limit = 1000 # Default account limit

# User entry to the App - check email and password
while True:
    user_email = input("Enter your email address : ")

    if '@' in user_email and '.' in user_email:
        print("Email Exists")
    else:
        print("Invalid Email, try again!")
        continue

    user_pin = input("Please enter your PIN : ")

    if len(user_pin) == 4 and user_pin.isdigit():
        print("User PIN accepted.")
        break

    else:
        print("Invalid PIN, try again")

print("Welcome! Please make a selection below : ")

print("""
1. Account Balance
2. Transfer funds
3. Deposit money
4. Withdraw Money
5. Check Account limits

""")

choice = input("Please make your selection (enter the number) : ")

# 1. Account balance check
if choice == '1':

    confirm_pin = input("Please enter your PIN to confirm action : ")

    if user_pin == confirm_pin:
        
        print(f"Your current balance is £{balance_current}")
    else:
        print("Incorrect PIN")

# 2. Transfer of funds
elif choice == '2':

    confirm_pin = input("Please enter your PIN to confirm action : ")

    if user_pin == confirm_pin:
        
        print(f"Your current balance is £{balance_current}")
        # User enters transfer details which are not checked immediately

        transfer_amount = int(input("Please enter how much you want to transfer : £ "))
        sort_code = int(input("Please enter 6-digit sort-code : "))
        transfer_account = input("Please enter the 10-digit account number : ")
        transfer_name = input("Please enter the account name : ")
        transfer_ref = input("Please enter the reference for the transfer : ")

        print(f"You are going to transfer £{transfer_amount} to {transfer_name} with bank details: {sort_code}, account {transfer_account}. The reference for the payment is {transfer_ref}")
        confirmation = int(input("Please confirm entering 1 if yes : "))

        if confirmation == 1:
        
            balance = balance_current - transfer_amount
            if balance >=0:
                print(f"Your new balance is £{balance}")
            else:
                print("You have insufficient amount for the transfer. Please try another amount.")

        else:
            print("The transfer is not confirmed. Please start again if you wish to make your transfer.")
    else:
        print("Incorrect PIN")

# 3. Money deposit
elif choice == '3':
    confirm_pin = input("Please enter your PIN to confirm action : ")

    if user_pin == confirm_pin:
        
        deposit = int(input("Please input the amount you want to deposit : £"))

        balance = balance_current+deposit
        print(f"Your new balance is £{balance}.")
    else:
        print("Incorrect PIN")

# 4. Money withdrawal
elif choice == '4':
    confirm_pin = input("Please enter your PIN to confirm action : ")

    if user_pin == confirm_pin:
        
        print(balance_current)
        withdrawal = int(input("Please enter the amount you want to withdraw : £"))
        if withdrawal <= balance_current:
            balance = balance_current-withdrawal
            print(f"Your new balance is £{balance}")
        else:
            print("You have insufficient funds to complete withdrawal. Please enter another amount.")
    else:
        print("Incorrect PIN") 

# 5. Check account limit
elif choice == '5':
    confirm_pin = input("Please enter your PIN to confirm action : ")

    if user_pin == confirm_pin:

        limit_option = int(input(f"Your account limit is £{account_limit}. Please enter '1' if you want to chage it."))
        if limit_option == 1:
            new_limit = int(input("Please enter options £500, £1000, or £1500 for the new account limit : £"))
            if new_limit == 500 or new_limit == 1000 or new_limit == 1500:
                print(f"Your new account limit is £{new_limit}")
            else:
                print("You entered invalid limit. Please try again.")
        else:
            print("Your account limit remains unchanged.")

        
    else:
        print("Incorrect PIN") 
else:
    print("You entered invalid number. Please try again.")

print("Thank you for your visit! Have a nice day!")              
