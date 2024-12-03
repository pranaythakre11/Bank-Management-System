<h1>Bank Account Management System</h1>

## Overview
The **Bank Account Management System** is a Python-based console application that allows users to manage bank accounts efficiently. It enables essential banking operations like account creation, depositing and withdrawing funds, transferring money, and viewing account details. The project is designed using object-oriented programming (OOP) principles and robust exception handling.

---

## Features
### Account Creation
- Create new accounts by providing:
  - Account Holder's Name
  - Unique Account Number
  - Account Type (Savings/Current)
  - Initial Deposit Amount

### Deposit Funds
- Deposit a specified positive amount into an existing account.
- Updates the account balance in real time.

### Withdraw Funds
- Withdraw a specified positive amount if the account has sufficient balance.

### Transfer Funds
- Transfer funds between two accounts.
- Validates the existence of both accounts and the sender's account balance.

### View Account Details
- Displays:
  - Account Holder's Name
  - Account Number
  - Account Type
  - Current Balance

### Command-Line Interface (CLI)
- Intuitive and user-friendly navigation through a menu-driven interface.

### Error Handling
- Handles exceptions and invalid inputs such as:
  - Duplicate account numbers.
  - Negative deposit or withdrawal amounts.
  - Insufficient balance for withdrawals or transfers.
  - Non-existent accounts for fund transfers.

---

## Technologies Used
- **Programming Language**: Python
- **Data Structures**: Dictionary for account storage
- **Paradigm**: Object-Oriented Programming (OOP)

---

