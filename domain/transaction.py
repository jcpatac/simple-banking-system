from datetime import datetime

class Transaction:
    latest_transaction_id = 0

    def __init__(self, account_id, amount, transaction_type):
        # Simple way of mimicking the auto-increment pk of databases
        Transaction.latest_transaction_id += 1
        self.transaction_id = Transaction.latest_transaction_id
        
        self.account_id = account_id
        self.amount = amount
        self.transaction_type = transaction_type
        self.timestamp = datetime.now()
