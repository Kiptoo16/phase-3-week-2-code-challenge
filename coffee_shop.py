class Coffee:
    all_coffees = []

    def __init__(self, name):
        # Directly assign to the private variable
        self._name = None  # Private variable to store the name
        self.name = name  # Use the property to set the name
        Coffee.all_coffees.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Coffee name must be a string.")
        if len(value) < 3:
            raise ValueError("Coffee name must be at least 3 characters long.")
        self._name = value  # Set the private variable

    def orders(self):
        return [order for order in Order.all_orders if order.coffee == self]

    def customers(self):
        return list({order.customer for order in self.orders()})  # Unique list of customers

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0
        total_price = sum(order.price for order in orders)
        return total_price / len(orders)

class Customer:
    all_customers = []

    def __init__(self, name):
        self.name = name  # Use property for validation
        self._orders = []  # Initialize orders list
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Customer name must be a string.")
        if len(value) < 1 or len(value) > 15:
            raise ValueError("Customer name must be between 1 and 15 characters.")
        self._name = value

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        self._orders.append(order)  # Keep track of the order
        return order

    def orders(self):
        return self._orders  # Return orders specific to the customer

    def coffees(self):
        return list({order.coffee for order in self.orders()})  # Unique coffees ordered by this customer

    @classmethod
    def most_aficionado(cls, coffee):
        customer_order_counts = {}
        
        for order in Order.all_orders:
            if order.coffee == coffee:
                customer_order_counts[order.customer] = customer_order_counts.get(order.customer, 0) + 1
        
        if not customer_order_counts:
            return None
        
        return max(customer_order_counts, key=customer_order_counts.get)

class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        self.customer = customer  # Validate with property
        self.coffee = coffee  # Validate with property
        self.price = price  # Validate with property
        Order.all_orders.append(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (float, int)) or not (1.0 <= value <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0.")
        self._price = value  # Set the private variable

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):
            raise ValueError("Customer must be a Customer instance.")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, Coffee):
            raise ValueError("Coffee must be a Coffee instance.")
        self._coffee = value
