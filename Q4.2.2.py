class BankAccount:
    def __init__(self, owner, balance=0):
        # Parameterized constructor to initialize object
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        # Add amount if positive
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New Balance: {self.balance}")
        else:
            print("Please enter a positive amount to deposit.")

    def withdraw(self, amount):
        # Withdraw only if enough balance
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New Balance: {self.balance}")
        else:
            print("Insufficient balance.")

    def __del__(self):
        # Destructor called when object is deleted
        print(f"Account for {self.owner} closed. Final balance was {self.balance}")

# Example usage
acc = BankAccount("Alice", 100)  # Initialize with name and balance
acc.deposit(50)
acc.withdraw(30)


