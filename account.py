class Account:
    # This is where your class attributes and methods will go 
    def __init__(self, account_holder, initial_balance=0):
        """
        Initializes a new bank account.

        Args:
            account_holder (str): The namem of the account holder.
            initial balance (int/float, optional): The starting balance. Defaults to 0.
        Raises:
            ValueError: If initial_balance is negative.
        """
        # 'self.account_holder' is an attribute that stores the account holder's name
        # 'self.balance' is an attribute that stores the account's balance
        # We ensure it's not negative initially
        
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.account_holder = account_holder
        self.balance = initial_balance
    
    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        Args:
            amount (int/float): The amount to deposit.
        Returns:
            str: A message indicating the deposit and new balance.
        Raises:
            ValueError: If the deposit amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return f"Deposited ${amount}. New Balance: ${self.balance}"
    
    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account.

        Args:
            amount (int/float): The amount to withdraw.
        Returns:
            str: A message indicating the withdrawal and new balance
        Raises:
            ValueError: If the withdrawal amount is not positive or insufficient funds.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return f"Withdrew ${amount}. New Balance: ${self.balance}"
    
    def get_balance(self):
        """
        Returns the current balance of the account.

        Returns:
            int/float: The current account balance.
        """
        return self.balance
    
    def get_account_holder(self):
        """
        Returns the name of the account holder.

        Returns:
            str: The account holder's name.
        """
        return self.account_holder


if __name__ == "__main":
    print("---Testing Account Class ---")

# Create and account
my_account = Account("Alice Smith", 100)
print(f"Account created for: {my_account.get_account_holder()}")
print(f"Initial balance: ${my_account.get_balance()}")

# Deposit money
print(my_account.deposit(50))

# Withdraw money
print(my_account.withdraw(30))

# Try to withdraw more than available
try:
    print(my_account.withdraw(200))
except ValueError as e:
    print(f"Error: {e}")

# Try invalid deposit
try:
    print(my_account.deposit(-10))
except ValueError as e:
    print(f"Error: {e}")

print(f"Final balance for {my_account.get_account_holder()}: ${my_account.get_balance()}")

# Create another account 
bob_account = Account("Bob Johnson") # Uses default initial_balance = 0
print(f"\nAccount created for: {bob_account.get_account_holder()}")
print(f"Initial balance: ${bob_account.get_balance()}")
bob_account.deposit(500)
print(f"Final balance for {bob_account.get_account_holder()}: ${bob_account.get_balance()}")

    

    


