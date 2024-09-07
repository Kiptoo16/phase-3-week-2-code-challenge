import pytest
from coffee_shop import Customer, Coffee, Order

def test_customer_initialization():
    customer = Customer("Kevin")
    assert customer.name == "Kevin"

    with pytest.raises(ValueError):
        Customer("")  
    with pytest.raises(ValueError):
        Customer("A" * 16)  

def test_coffee_initialization():
    coffee = Coffee("Capuchino")
    assert coffee.name == "Capuchino"

    with pytest.raises(ValueError):
        Coffee("AB")  

def test_order_initialization():
    customer = Customer("Kevin")
    coffee = Coffee("Capuchino")
    order = Order(customer, coffee, 4.5)
    
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 4.5

    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)  
    with pytest.raises(ValueError):
        Order(customer, coffee, 10.5)  

def test_customer_orders():

    Customer.all_customers = []
    

    customer = Customer("Kevin")
    coffee = Coffee("Capuchino")
    

    customer.create_order(coffee, 4.5)
    
    
    print("Created Orders: ", [order for order in customer.orders()])

    

    orders = customer.orders()
    assert len(orders) == 2
    assert orders[0].price == 4.5
    assert orders[0].coffee == coffee
    assert orders[0].customer == customer


def test_customer_coffees():
    customer = Customer("Kevin")
    coffee1 = Coffee("Capuchino")
    coffee2 = Coffee("Espresso")
    customer.create_order(coffee1, 4.5)
    customer.create_order(coffee2, 3.0)
    
    assert len(customer.coffees()) == 2
    assert coffee1 in customer.coffees()
    assert coffee2 in customer.coffees()

def test_coffee_orders():
    coffee = Coffee("Capuchino")
    customer1 = Customer("Kevin")
    customer2 = Customer("Dee")
    order1 = customer1.create_order(coffee, 4.5)
    order2 = customer2.create_order(coffee, 5.0)
    
    assert len(coffee.orders()) == 2
    assert order1 in coffee.orders()
    assert order2 in coffee.orders()

def test_coffee_customers():
    coffee = Coffee("Capuchino")
    customer1 = Customer("Kevin")
    customer2 = Customer("Dee")
    customer1.create_order(coffee, 4.5)
    customer2.create_order(coffee, 5.0)
    
    assert len(coffee.customers()) == 2
    assert customer1 in coffee.customers()
    assert customer2 in coffee.customers()

def test_coffee_num_orders():
    coffee = Coffee("Capuchino")
    customer1 = Customer("Kevin")
    customer2 = Customer("Dee")
    customer1.create_order(coffee, 4.5)
    customer2.create_order(coffee, 5.0)
    
    assert coffee.num_orders() == 2

def test_coffee_average_price():
    coffee = Coffee("Capuchino")
    customer1 = Customer("Kevin")
    customer2 = Customer("Dee")
    customer1.create_order(coffee, 4.5)
    customer2.create_order(coffee, 5.0)
    
    assert coffee.average_price() == 4.75

def test_most_aficionado():
    coffee = Coffee("Capuchino")
    customer1 = Customer("Kevin")
    customer2 = Customer("Dee")
    customer1.create_order(coffee, 4.5)
    customer1.create_order(coffee, 5.0)
    customer2.create_order(coffee, 3.0)
    
    assert Customer.most_aficionado(coffee) == customer1
