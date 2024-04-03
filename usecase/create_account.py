from domain import Account, Customer
import random, string

class CreateAccountUseCase:
    def __init__(self, account_repository, customer_repository):
        self.account_repository = account_repository
        self.customer_repository = customer_repository

    @staticmethod
    def _generate_account_number(customer):
        # later on, we can use other means to include the customer
        # details to generate the account number
        random_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        account_number = f'{random_str}-{customer.customer_id}'
        return account_number
    
    def get_or_create_customer(self, customer_id, name, email, phone_number):
        created = False
        customer = self.customer_repository.find_customer_by_id(
            customer_id=customer_id)
        if not customer:
            customer = Customer(
                customer_id=customer_id,
                name=name,
                email=email,
                phone_number=phone_number
            )
            # add the new customer to the repo
            self.customer_repository.save_customer(customer=customer)
            created = True
        
        return created, customer

    def create_account(self, customer_id, name, email, phone_number):
        # create new customer if non-existing
        # else, just use the existing account
        _, customer = self.get_or_create_customer(
            customer_id, name, email, phone_number)
        
        # create a new account for the customer
        account_number = self._generate_account_number(customer)
        account = Account(
            customer_id=customer.customer_id,
            account_number=account_number
        )
        # add the new account to the repo
        self.account_repository.save_account(account=account)
        return account
