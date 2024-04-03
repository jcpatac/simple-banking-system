class MakeTransactionUseCase:
    """
    Use case for making transactions on accounts.

    Attributes:
        account_repository: Repository for managing accounts.
    """

    def __init__(self, account_repository):
        self.account_repository = account_repository

    def make_transaction(self, account_id, amount, transaction_type):
        """
        Makes a transaction on the specified account.

        Parameters:
            account_id: ID of the account.
            amount: Amount of the transaction.
            transaction_type: Type of transaction (e.g., 'deposit', 'withdraw').

        Returns:
            str: A message indicating the result of the transaction.
        
        Raises:
            KeyError: If the account is not found.
        """

        account = self.account_repository.find_account_by_id(account_id=account_id)
        if not account:
            raise KeyError('Account not found!')
        
        if transaction_type.lower() == 'deposit':
            result = account.deposit(amount)
        elif transaction_type.lower() == 'withdraw':
            result = account.withdraw(amount)
        else:
            result = 'Invalid transaction type!'
        self.account_repository.save_account(account=account)
        return result
