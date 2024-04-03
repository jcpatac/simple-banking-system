import unittest
from infrastructure import (AccountRepository, CustomerRepository)
from usecase import (
    CreateAccountUseCase
)


class TestCustomerRepository(unittest.TestCase):

    def setUp(self):
        # initialize the repositories
        self.customer_repository = CustomerRepository()
        # use cases
        self.create_account_use_case = CreateAccountUseCase(
            None, self.customer_repository)

        self.customer_data = [
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
            **self.customer_data[0]
        )
        _, self.customer_2 = self.create_account_use_case.get_or_create_customer(
            **self.customer_data[1]
        )
    
    def test_save_customer(self):
        # get_or_create_customer uses save_customer
        customer_count = len(self.customer_repository.customers)

        self.assertEqual(len(self.customer_data), customer_count)
    
    def test_find_customer_by_id(self):
        customer = self.customer_repository.find_customer_by_id(
            self.customer_1.customer_id)
        
        self.assertEqual(customer.customer_id, self.customer_1.customer_id)


class TestAccountRepository(unittest.TestCase):

    def setUp(self):
        # initialize the repositories
        self.customer_repository = CustomerRepository()
        self.account_repository = AccountRepository()
        # use cases
        self.create_account_use_case = CreateAccountUseCase(
            self.account_repository, self.customer_repository)

        self.customer_data = [
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

        self.account_1 = self.create_account_use_case.create_account(
            **self.customer_data[0]
        )
        self.account_1_a = self.create_account_use_case.create_account(
            **self.customer_data[0]
        )
        self.account_2 = self.create_account_use_case.create_account(
            **self.customer_data[1]
        )
    
    def test_save_account(self):
        # create_account uses save_account
        account_count = len(self.account_repository.accounts)

        # 3 because we created 2 accounts for customer_data[0]
        self.assertEqual(3, account_count)
    
    def test_find_account_by_id(self):
        account = self.account_repository.find_account_by_id(
            self.account_2.account_id)
        
        self.assertEqual(account.account_id, self.account_2.account_id)
    
    def test_find_accounts_by_customer_id(self):
        accounts = self.account_repository.find_accounts_by_customer_id(
            self.customer_data[0].get('customer_id')
        )

        self.assertEqual(len(accounts), 2)
    
    def test_get_all_accounts(self):
        accounts = self.account_repository.get_all_accounts()

        self.assertEqual(len(accounts), 3)
