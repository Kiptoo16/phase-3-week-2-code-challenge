class Customer:
    all_customers = []

    def __init__(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise ValueError
        self._name = name
        self._orders = []
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 15):
            raise ValueError
        self._name = value

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    def create_order(self, coffee, price):
        if not isinstance(price, (int, float)) or not (1.0 <= price <= 10.0):
            raise ValueError
        order = Order(self, coffee, price)
        self._orders.append(order)
        return order


    @classmethod
    def most_aficionado(cls, coffee):
        if not coffee.orders():
            return None
        customer_spending = {}
        for customer in cls.all_customers:
            total_spent = sum(order.price for order in customer.orders() if order.coffee == coffee)
            if total_spent > 0:
                customer_spending[customer] = total_spent
        if customer_spending:
            return max(customer_spending, key=customer_spending.get)
        return None



class Coffee:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError

    def orders(self):
        return self._orders

    def customers(self):
        return list(set(order.customer for order in self._orders))

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0
        return sum(order.price for order in self._orders) / len(self._orders)


class Order:
    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise ValueError
        if not isinstance(coffee, Coffee):
            raise ValueError
        if not isinstance(price, (int, float)) or not (1.0 <= price <= 10.0):
            raise ValueError
        self._customer = customer
        self._coffee = coffee
        self._price = price
        coffee._orders.append(self)
        customer._orders.append(self)

    @property
    def price(self):
        return self._price

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee
