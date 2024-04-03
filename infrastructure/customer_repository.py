class CustomerRepository:

    def __init__(self):
        self.customers = {}
    
    def save_customer(self, customer):
        self.customers[customer.customer_id] = customer
    
    def find_customer_by_id(self, customer_id):
        return self.customers.get(customer_id, None)
