# created from response - used to create database and project
#  should run without error
#  if not, check for decimal, indent, or import issues

import decimal

import logging



logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

import sqlalchemy



from sqlalchemy.sql import func  # end imports from system/genai/create_db_models_inserts/create_db_models_prefix.py

from logic_bank.logic_bank import Rule

from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker
import datetime

# Define the base class
Base = declarative_base()

# Define the database models
class Company(Base):
    """description: Represents a company entity containing company details."""
    __tablename__ = 'companies'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    
class Department(Base):
    """description: Departments in a company, associated with employees."""
    __tablename__ = 'departments'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    company_id = Column(Integer, ForeignKey('companies.id'), nullable=False)

class Employee(Base):
    """description: Employees working within various departments in a company."""
    __tablename__ = 'employees'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id'), nullable=False)

class Product(Base):
    """description: Products offered by the company."""
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))

class Order(Base):
    """description: Customer orders of products."""
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    date_created = Column(DateTime, default=func.now())
    customer_id = Column(Integer, ForeignKey('customers.id'))
    employee_id = Column(Integer, ForeignKey('employees.id'))

class Customer(Base):
    """description: Company's customers, placing orders."""
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)

class Supplier(Base):
    """description: Suppliers providing products to the company."""
    __tablename__ = 'suppliers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

class Inventory(Base):
    """description: Inventory table tracking product stock levels."""
    __tablename__ = 'inventory'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer, nullable=False)

class Shipment(Base):
    """description: Shipments made for orders."""
    __tablename__ = 'shipments'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    shipped_date = Column(DateTime, default=func.now())

class Invoice(Base):
    """description: Invoices issued for customer orders."""
    __tablename__ = 'invoices'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    total_amount = Column(Float, nullable=False)

class Payment(Base):
    """description: Payments received from customers for orders."""
    __tablename__ = 'payments'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    invoice_id = Column(Integer, ForeignKey('invoices.id'))
    amount_paid = Column(Float, nullable=False)
    payment_date = Column(DateTime, default=func.now())

class Project(Base):
    """description: Company projects, involving employees."""
    __tablename__ = 'projects'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    budget = Column(Float)
    department_id = Column(Integer, ForeignKey('departments.id'))

# Create an SQLite database
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite', echo=False)

# Create tables in the database
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Insert sample data
# Companies
company1 = Company(name="TechCorp")
session.add(company1)

# Departments
department1 = Department(name="Research", company_id=1)
department2 = Department(name="Sales", company_id=1)
session.add_all([department1, department2])

# Employees
employee1 = Employee(name="John Smith", department_id=1)
employee2 = Employee(name="Jane Doe", department_id=2)
session.add_all([employee1, employee2])

# Suppliers
supplier1 = Supplier(name="Supplier A")
session.add(supplier1)

# Products
product1 = Product(name="Gadget", price=99.99, supplier_id=1)
product2 = Product(name="Widget", price=49.99, supplier_id=1)
session.add_all([product1, product2])

# Inventory
inventory1 = Inventory(product_id=1, quantity=100)
inventory2 = Inventory(product_id=2, quantity=200)
session.add_all([inventory1, inventory2])

# Customers
customer1 = Customer(name="ABC Inc.", email="contact@abcinc.com")
session.add(customer1)

# Orders
order1 = Order(customer_id=1, employee_id=1)
session.add(order1)

# Shipments
shipment1 = Shipment(order_id=1, shipped_date=datetime.datetime(2023, 10, 1))
session.add(shipment1)

# Invoices
invoice1 = Invoice(order_id=1, total_amount=149.98)
session.add(invoice1)

# Payments
payment1 = Payment(invoice_id=1, amount_paid=149.98, payment_date=datetime.datetime(2023, 10, 5))
session.add(payment1)

# Projects
project1 = Project(name="Project X", budget=15000, department_id=1)
session.add(project1)

# Commit session
session.commit()

# Close session
session.close()
