from usecase import (
    CreateAccountUseCase,
    MakeTransactionUseCase,
    GenerateAccountStatementUseCase)
from infrastructure import (
    AccountRepository,
    CustomerRepository
)


def main():
    """
        This might not cover all scenario
        Please checkout tests folder for other scenarios
    """

    print('... RUNNING SAMPLES FOR SIMPLE BANKING SYSTEM ...')
    # initialize the repositories
    account_repository = AccountRepository()
    customer_repository = CustomerRepository()

    # create customers
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
    
    # use cases
    create_account_use_case = CreateAccountUseCase(
        account_repository, customer_repository)
    make_transaction_use_case = MakeTransactionUseCase(
        account_repository)
    generate_statement_use_case = GenerateAccountStatementUseCase(
        account_repository, customer_repository
    )

    # create accounts
    # we have auto-creation of customers the data given is non-existing
    for data in customer_data:
        create_account_use_case.create_account(**data)
    
    # perform transactions
    # ACCOUNT 1
    acct_1_txn_1 = make_transaction_use_case.make_transaction(
        account_id=1,
        amount=1000,
        transaction_type='deposit'
    )
    acct_1_txn_2 = make_transaction_use_case.make_transaction(
        account_id=1,
        amount=300,
        transaction_type='withdraw'
    )
    acct_1_txn_3 = make_transaction_use_case.make_transaction(
        account_id=1,
        amount=500,
        transaction_type='withdraw'
    )    
    # EXPECTED FINAL BALANCE IN STATEMENT: 200
    # ACCOUNT 2
    acct_2_txn_1 = make_transaction_use_case.make_transaction(
        account_id=2,
        amount=2000,
        transaction_type='deposit'
    )
    acct_2_txn_2 = make_transaction_use_case.make_transaction(
        account_id=2,
        amount=2000,
        transaction_type='withdraw'
    )
    # EXPECTED FINAL BALANCE IN STATEMENT: 0

    # SHOULD RETURN INSUFFICIENT BALANCE
    acct_1_txn_4 = make_transaction_use_case.make_transaction(
        account_id=1,
        amount=500,
        transaction_type='withdraw'
    )
    print('>>>', acct_1_txn_4)

    # generate statements
    statement_1 = generate_statement_use_case.generate_account_statement(
        account_id=1
    )
    statement_2 = generate_statement_use_case.generate_account_statement(
        account_id=2
    )
    print('\n\n>>> PRINTING STATEMENTS...\n\n')
    print(statement_1)
    print(statement_2)



if __name__ == '__main__':
    main()
