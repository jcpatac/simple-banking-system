class Customer:
    """
    Represents a customer with basic information.

    Attributes:
        customer_id: ID of the customer.
        name: Name of the customer.
        email: Email address of the customer.
        phone_number: Phone number of the customer.
    """

    def __init__(self, customer_id, name, email, phone_number):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone_number = phone_number
