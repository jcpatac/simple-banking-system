from .transaction import Transaction

class Account:
    latest_account_id = 0

    def __init__(self, customer_id, account_number, balance=0):
        # Simple way of mimicking the auto-increment pk of databases
        Account.latest_account_id += 1
        self.account_id = Account.latest_account_id
        
        self.customer_id = customer_id
        self.account_number = account_number
        self.balance = balance

        # we'll be using this to track transaction history
        # this can be FK irl
        self.transactions = []
    
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(
            Transaction(
                account_id=self.account_id,
                amount=amount,
                transaction_type='deposit'
            )
        )
        return 'Successful deposit'
    
    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient balance!'
        
        self.balance -= amount
        self.transactions.append(
            Transaction(
                account_id=self.account_id,
                amount=(-amount),
                transaction_type='withdraw'
            )
        )
        return amount
    
    def get_balance(self):
        return self.balance
