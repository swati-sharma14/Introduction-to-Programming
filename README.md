💰 Bank Account Management 

Welcome to the Bank Account Management program of the Bank of IIIT-Delhi! This program allows you to create a bank account, perform various transactions such as deposits and withdrawals, and view your transaction history.


📝 Description

The program consists of a BankAccount class that represents a bank account. Each instance of the class represents an individual's account and contains the following information:

  - Name: Name of the account holder
  - Password: Secret password for authentication
  - Current Balance: Current balance in the account
  
The class provides the following methods:

1. authenticate(): Authenticates the account holder by checking the provided password against the stored password. Allows for a limited number of wrong attempts before blocking the account.
2. deposit(): Deposits a specified amount of money into the account if the authentication is successful. Updates the current balance and logs the transaction in a text file.
3. withdraw(): Withdraws a specified amount of money from the account if the authentication is successful and the account balance is sufficient. Updates the current balance and logs the transaction in a text file.
4. bankStatement(): Displays the transaction history of the account.


🛠️ Usage

1. Run the program.
2. Provide your name, password, and the starting balance of your account.
3. Select one of the following options:
    - Deposit: Enter 1 and provide the amount to be deposited.
    - Withdraw: Enter 2 and provide the amount to be withdrawn.
    - Bank Statement: Enter 3 to view the transaction history.
4. Depending on your choice, follow the prompts to complete the desired transaction or view the bank statement.
5. After completing a transaction, you will be prompted to continue or exit the program.
