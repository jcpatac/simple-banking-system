from datetime import datetime

class Transaction:
    """
    Represents a transaction associated with a bank account.

    Attributes:
        latest_transaction_id: Class variable for tracking the latest transaction ID.
        transaction_id: Unique identifier of the transaction.
        account_id: ID of the account associated with the transaction.
        amount: Amount involved in the transaction.
        transaction_type: Type of transaction (e.g., deposit, withdrawal).
        timestamp: Date and time when the transaction occurred.
    """

    latest_transaction_id = 0

    def __init__(self, account_id, amount, transaction_type):
        # Simple way of mimicking the auto-increment pk of databases
        Transaction.latest_transaction_id += 1
        self.transaction_id = Transaction.latest_transaction_id
        
        self.account_id = account_id
        self.amount = amount
        self.transaction_type = transaction_type
        self.timestamp = datetime.now()
