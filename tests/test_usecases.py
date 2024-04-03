import unittest
from infrastructure import (AccountRepository, CustomerRepository)
from usecase import (
    CreateAccountUseCase,
    MakeTransactionUseCase,
    GenerateAccountStatementUseCase
)


class TestUsecases(unittest.TestCase):

    def setUp(self):
        # initialize the repositories
        self.account_repository = AccountRepository()
        self.customer_repository = CustomerRepository()

        # use cases
        self.create_account_use_case = CreateAccountUseCase(
            self.account_repository, self.customer_repository)
        self.make_transaction_use_case = MakeTransactionUseCase(
            self.account_repository)
        self.generate_statement_use_case = GenerateAccountStatementUseCase(
            self.account_repository, self.customer_repository
        )

        customer_data = [
            {
                'customer_id': 1,
                'name': 'Sheldon Cooper',
                'email': 'shelly@example.com',
                'phone_number': '12345'
            },
            {
                'customer_id': 2,
                'name': 'Missy Cooper',
                'email': 'missy@example.com',
                'phone_number': '67890'
            }
        ]

        _, self.customer_1 = self.create_account_use_case.get_or_create_customer(
            **customer_data[0]
        )
        _, self.customer_2 = self.create_account_use_case.get_or_create_customer(
            **customer_data[1]
        )
    
    def test_account_creation(self):
        account_1 = self.create_account_use_case.create_account(
            self.customer_1.customer_id,
            self.customer_1.name,
            self.customer_1.email,
            self.customer_1.phone_number
        )
        account_2 = self.create_account_use_case.create_account(
            self.customer_2.customer_id,
            self.customer_2.name,
            self.customer_2.email,
            self.customer_2.phone_number
        )

        self.assertIsNotNone(account_1)
        self.assertIsNotNone(account_2)
        self.assertEqual(account_1.customer_id, self.customer_1.customer_id)
        self.assertEqual(account_2.customer_id, self.customer_2.customer_id)
    
    def test_non_existing_accounts(self):
        non_existing_id = 10000
        self.assertIsNone(self.account_repository.find_account_by_id(non_existing_id))
    
    def test_no_txn_statement(self):
        account_1 = self.create_account_use_case.create_account(
            self.customer_2.customer_id,
            self.customer_2.name,
            self.customer_2.email,
            self.customer_2.phone_number
        )
        statement = self.generate_statement_use_case.generate_account_statement(
            account_id=account_1.account_id
        )

        self.assertIn('This account has no transaction history!', statement)

    def test_transactions_and_statement(self):
        account_1 = self.create_account_use_case.create_account(
            self.customer_1.customer_id,
            self.customer_1.name,
            self.customer_1.email,
            self.customer_1.phone_number
        )
        self.make_transaction_use_case.make_transaction(
            account_id=account_1.account_id,
            amount=1000,
            transaction_type='deposit'
        )
        self.make_transaction_use_case.make_transaction(
            account_id=account_1.account_id,
            amount=900,
            transaction_type='withdraw'
        )
        statement = self.generate_statement_use_case.generate_account_statement(
            account_id=account_1.account_id
        )

        self.assertIn('Type: deposit', statement)
        self.assertIn('Type: withdraw', statement)
        self.assertIn('Amount: 1000', statement)
        self.assertIn('Amount: -900', statement)
    
    def test_fail_withdraw_transaction(self):
        account_2 = self.create_account_use_case.create_account(
            self.customer_2.customer_id,
            self.customer_2.name,
            self.customer_2.email,
            self.customer_2.phone_number
        )
        self.make_transaction_use_case.make_transaction(
            account_id=account_2.account_id,
            amount=1000,
            transaction_type='deposit'
        )
        withdraw_amt = 2000
        withdraw_txn = self.make_transaction_use_case.make_transaction(
            account_id=account_2.account_id,
            amount=withdraw_amt,
            transaction_type='withdraw'
        )

        self.assertIn('Insufficient balance!', withdraw_txn)
