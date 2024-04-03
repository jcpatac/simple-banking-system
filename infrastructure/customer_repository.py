class CustomerRepository:
    """
    Repository for managing customers.

    Attributes:
        customers: Dictionary to store customers with customer ID as key.
    """

    def __init__(self):
        self.customers = {}
    
    def save_customer(self, customer):
        """
        Saves the given customer in the repository.

        Parameters:
            customer: A Customer object to be saved.
        """

        self.customers[customer.customer_id] = customer
    
    def find_customer_by_id(self, customer_id):
        """
        Finds a customer by their ID.

        Parameters:
            customer_id: ID of the customer to be found.

        Returns:
            Customer: The found customer or None if not found.
        """

        return self.customers.get(customer_id, None)
