# COFFEE SHOP CODE CHALLENGE

Welcome to the Coffee Shop Code Challenge! This project demonstrates object-oriented programming in Python by modeling a simple coffee shop system with classes for Customer, Coffee, and Order.

# Contents
Installation
Usage
Testing
Code Structure
Contributing
License

# Project Overview
The Coffee Shop project includes three main classes:

Customer: Represents a customer who can place orders.
Coffee: Represents a type of coffee available in the shop.
Order: Represents an order placed by a customer for a specific coffee.

# Relationships
A Customer can place multiple Orders.
A Coffee can be ordered multiple times.
Each Order is linked to one Customer and one Coffee.

# Installation
To get started with this project, follow these steps:

Clone the Repository: 
git clone [https://github.com/Kiptoo16/phase-3-week-2-code-challenge.git]
cd phase-3-week-2-code-challenge
Set Up a Virtual Environment

Install Dependencies

This project does not have external dependencies beyond Python's standard library, but you should install pytest for testing:

# pip install pytest
Usage
To use the coffee shop classes, you can interact with them through a Python interpreter or write a script. Here’s a basic example:

from coffee_shop import Customer, Coffee, Order

# Create instances
customer = Customer("Kevin")
coffee = Coffee("Capuchino")

# Place an order
order = customer.create_order(coffee, 4.5)

# Access information
print(f"Customer {customer.name} has ordered {order.coffee.name} for ${order.price}.")
print(f"Total orders for coffee: {coffee.num_orders()}")
print(f"Average price of coffee: {coffee.average_price()}")

# Testing
To ensure that everything works as expected, you can run the test suite using pytest. The tests are located in test_coffee_shop.py.

Run Tests

# pytest
This will execute all the test cases defined in the test_coffee_shop.py file.

# Code Structure
coffee_shop.py: Contains the definitions for the Customer, Coffee, and Order classes.
test_coffee_shop.py: Contains unit tests for the classes to ensure functionality.

# License
This project is licensed under the MIT License. See the LICENSE file for details.

@Kevin Langat c2024
