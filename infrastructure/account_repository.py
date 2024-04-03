class AccountRepository:
    """
    Repository for managing bank accounts.

    Attributes:
        accounts: Dictionary to store accounts with account ID as key.
    """

    def __init__(self):
        self.accounts = {}
    
    def save_account(self, account):
        """
        Saves the given account in the repository.

        Parameters:
            account: An Account object to be saved.
        """
        self.accounts[account.account_id] = account
    
    def find_account_by_id(self, account_id):
        """
        Finds an account by its ID.

        Parameters:
            account_id: ID of the account to be found.

        Returns:
            Account: The found account or None if not found.
        """
        return self.accounts.get(account_id, None)
    
    def find_accounts_by_customer_id(self, customer_id):
        """
        Finds accounts associated with a specific customer.

        Parameters:
            customer_id: ID of the customer.

        Returns:
            list: List of Account objects associated with the customer.
        """
        return [
            account for account in self.accounts.values()
            if account.customer_id == customer_id
        ]
    
    def get_all_accounts(self):
        """
        Retrieves all accounts stored in the repository.

        Returns:
            list: List of dictionaries representing accounts.
        """
        all_accounts = []
        for _, val in self.accounts.items():
            all_accounts.append(vars(val))
        return all_accounts
