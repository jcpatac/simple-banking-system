class GenerateAccountStatementUseCase:
    def __init__(self, account_repository, customer_repository):
        self.account_repository = account_repository
        self.customer_repository = customer_repository

    def generate_account_statement(self, account_id):
        account = self.account_repository.find_account_by_id(account_id)
        if not account:
            raise KeyError('Account not found!')
        
        customer = self.customer_repository.find_customer_by_id(
            account.customer_id)
        if not customer:
            raise KeyError('Customer not found!')

        return self._format_account_statement(
            account, customer)
    
    @staticmethod
    def _format_account_statement(account, customer):
        if not len(account.transactions):
            return 'This account has no transaction history!'

        statement = (
            f'Account Statement for Account ID: { account.account_id }\n'
            f'Account Number: { account.account_number }\n'
            f'Account Name: { customer.name }\n'
            'Transactions:\n'
        )
        for transaction in account.transactions:
            statement += (
                f'   Transaction ID: { transaction.transaction_id }\n'
                f'   Type: { transaction.transaction_type }\n'
                f'   Amount: { transaction.amount }\n'
                f'   Transaction Date: { transaction.timestamp }\n\n'
                f'   *********************************************\n\n'
            )
        
        statement += f'Current Account Balance: { account.get_balance() }\n\n'
        statement += ('-' * 20) + ' END OF STATEMENT ' + ('-' * 20)
        return statement
