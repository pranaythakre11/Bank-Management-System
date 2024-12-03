# bank_management_system.py

# Created Class to represent bank account
class Account:
    # Created Constructor to initialize account details such as name, number, type, balance
    def __init__(self, holder_name, account_number, account_type, balance=0):
        self.holder_name = holder_name        # Name of the account holder
        self.account_number = account_number  # Unique account number
        self.account_type = account_type      # Type of account (Savings/Current)
        self.balance = balance                # Current balance which starts with initial deposit

    # Created Method to deposit money into the account
    def deposit(self, amount):
        if amount > 0:             
            self.balance += amount  
            print(f"Deposit successful! New Balance: {self.balance}")
        else:
            print("Error: Deposit amount must be positive.")

    # Method to withdraw money from the account
    def withdraw(self, amount):
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")  
        elif amount > self.balance:
            print("Error: Insufficient balance.")  
        else:
            self.balance -= amount                  # Deduct the withdrawal amount from balance
            print(f"Withdrawal successful! New Balance: {self.balance}")

    # Method to display the account details
    def display_details(self):
        print(f"Account Holder: {self.holder_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Current Balance: {self.balance}")

# Class to manage the overall bank system and multiple accounts
class BankSystem:
    # Constructor to initialize an empty dictionary to store accounts
    def __init__(self):
        self.accounts = {}  # Dictionary for storeing accountsdetaild using account number as the key

    # Method to create a new account
    def create_account(self):
        holder_name = input("Enter Account Holder's Name: ")  # Take account holder name as input
        while True:
            try:
                account_number = int(input("Enter Account Number: "))  # Input and convert to integer
                if account_number in self.accounts:  # Check if account number already exists
                    raise ValueError("Account number already exists.")  # Raise error if duplicate
                break  # Exit the loop if account number is valid
            except ValueError as e:
                print(f"Error: {e}")  # Display error message

        account_type = input("Enter Account Type (Savings/Current): ").capitalize()  # Get and capitalize account type
        while True:
            try:
                initial_deposit = float(input("Enter Initial Deposit Amount: "))  # Input initial deposit
                if initial_deposit < 0:  # Check if deposit is negative
                    raise ValueError("Initial deposit cannot be negative.")  # Raise error for invalid amount
                break
            except ValueError as e:
                print(f"Error: {e}")  # Display error message

        # Create a new Account object and store it in the dictionary
        self.accounts[account_number] = Account(holder_name, account_number, account_type, initial_deposit)
        print("Account created successfully!")

    # Method to deposit funds into an account
    def deposit_funds(self):
        try:
            account_number = int(input("Enter Account Number: "))  # Input account number
            if account_number not in self.accounts:  # Check if account exists
                raise ValueError("Account does not exist.")  # Raise error if account not found

            amount = float(input("Enter Amount to Deposit: "))  # Input deposit amount
            self.accounts[account_number].deposit(amount)  # Call the deposit method of the account
        except ValueError as e:
            print(f"Error: {e}")  # Display error message

    # Method to withdraw funds from an account
    def withdraw_funds(self):
        try:
            account_number = int(input("Enter Account Number: "))  # Input account number
            if account_number not in self.accounts:  # Check if account exists
                raise ValueError("Account does not exist.")  # Raise error if account not found

            amount = float(input("Enter Amount to Withdraw: "))  # Input withdrawal amount
            self.accounts[account_number].withdraw(amount)  # Call the withdraw method of the account
        except ValueError as e:
            print(f"Error: {e}")  # Display error message

    # Method to transfer funds from one account to another
    def transfer_funds(self):
        try:
            sender_account = int(input("Enter Sender's Account Number: "))  # Input sender's account number
            if sender_account not in self.accounts:  # Check if sender's account exists
                raise ValueError("Sender's account does not exist.")  # Raise error if not found

            receiver_account = int(input("Enter Receiver's Account Number: "))  # Input receiver's account number
            if receiver_account not in self.accounts:  # Check if receiver's account exists
                raise ValueError("Receiver's account does not exist.")  # Raise error if not found

            amount = float(input("Enter Amount to Transfer: "))  # Input transfer amount
            if amount <= 0:
                raise ValueError("Transfer amount must be positive.")  # Raise error for negative transfer
            if self.accounts[sender_account].balance < amount:  # Check if sender has enough balance
                raise ValueError("Insufficient balance in sender's account.")

            # Process the transfer
            self.accounts[sender_account].withdraw(amount)  # Withdraw from sender's account
            self.accounts[receiver_account].deposit(amount)  # Deposit into receiver's account
            print(f"Transfer successful! {amount} transferred from Account {sender_account} to Account {receiver_account}.")
        except ValueError as e:
            print(f"Error: {e}")  # Display error message

    # Method to view the details of an account
    def view_account_details(self):
        try:
            account_number = int(input("Enter Account Number: "))  # Input account number
            if account_number not in self.accounts:  # Check if account exists
                raise ValueError("Account does not exist.")  # Raise error if not found

            self.accounts[account_number].display_details()  # Call display method to show account details
        except ValueError as e:
            print(f"Error: {e}")  # Display error message

    # Method to run the bank system and provide a menu to the user
    def run(self):
        while True:  # Infinite loop to keep the system running until user exits
            # Display the menu options
            print("\n--------------------------------------------")
            print("Welcome to the Bank Account Management System")
            print("--------------------------------------------")
            print("Please select an option:")
            print("1. Create New Account")
            print("2. Deposit Funds")
            print("3. Withdraw Funds")
            print("4. Transfer Funds")
            print("5. View Account Details")
            print("6. Exit")

            try:
                choice = int(input("Enter your choice: "))  # Input user's choice
                # Call appropriate method based on user's choice
                if choice == 1:
                    self.create_account()
                elif choice == 2:
                    self.deposit_funds()
                elif choice == 3:
                    self.withdraw_funds()
                elif choice == 4:
                    self.transfer_funds()
                elif choice == 5:
                    self.view_account_details()
                elif choice == 6:
                    print("Thank you for using the Bank Account Management System. Goodbye!")
                    break  # Exit the loop and end the program
                else:
                    print("Error: Invalid option selected.")  # Handle invalid menu options
            except ValueError:
                print("Error: Please enter a valid numeric option.")  # Handle non-numeric inputs

# Entry point of the program
if __name__ == "__main__":
    bank_system = BankSystem()  # Create an instance of the BankSystem class
    bank_system.run()  # Start the bank system
