# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  November 08, 2024 05:45:16
# Database: sqlite:////tmp/tmp.TPuTS33X8b/genai_01JC54VRT6ZSA0HY45HHHN2MRA/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Company(SAFRSBaseX, Base):
    """
    description: Represents a company entity containing company details.
    """
    __tablename__ = 'companies'
    _s_collection_name = 'Company'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    DepartmentList : Mapped[List["Department"]] = relationship(back_populates="company")



class Customer(SAFRSBaseX, Base):
    """
    description: Company's customers, placing orders.
    """
    __tablename__ = 'customers'
    _s_collection_name = 'Customer'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    OrderList : Mapped[List["Order"]] = relationship(back_populates="customer")



class Supplier(SAFRSBaseX, Base):
    """
    description: Suppliers providing products to the company.
    """
    __tablename__ = 'suppliers'
    _s_collection_name = 'Supplier'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    ProductList : Mapped[List["Product"]] = relationship(back_populates="supplier")



class Department(SAFRSBaseX, Base):
    """
    description: Departments in a company, associated with employees.
    """
    __tablename__ = 'departments'
    _s_collection_name = 'Department'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    company_id = Column(ForeignKey('companies.id'), nullable=False)

    # parent relationships (access parent)
    company : Mapped["Company"] = relationship(back_populates=("DepartmentList"))

    # child relationships (access children)
    EmployeeList : Mapped[List["Employee"]] = relationship(back_populates="department")
    ProjectList : Mapped[List["Project"]] = relationship(back_populates="department")



class Product(SAFRSBaseX, Base):
    """
    description: Products offered by the company.
    """
    __tablename__ = 'products'
    _s_collection_name = 'Product'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    supplier_id = Column(ForeignKey('suppliers.id'))

    # parent relationships (access parent)
    supplier : Mapped["Supplier"] = relationship(back_populates=("ProductList"))

    # child relationships (access children)
    InventoryList : Mapped[List["Inventory"]] = relationship(back_populates="product")



class Employee(SAFRSBaseX, Base):
    """
    description: Employees working within various departments in a company.
    """
    __tablename__ = 'employees'
    _s_collection_name = 'Employee'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    department_id = Column(ForeignKey('departments.id'), nullable=False)

    # parent relationships (access parent)
    department : Mapped["Department"] = relationship(back_populates=("EmployeeList"))

    # child relationships (access children)
    OrderList : Mapped[List["Order"]] = relationship(back_populates="employee")



class Inventory(SAFRSBaseX, Base):
    """
    description: Inventory table tracking product stock levels.
    """
    __tablename__ = 'inventory'
    _s_collection_name = 'Inventory'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    product_id = Column(ForeignKey('products.id'))
    quantity = Column(Integer, nullable=False)

    # parent relationships (access parent)
    product : Mapped["Product"] = relationship(back_populates=("InventoryList"))

    # child relationships (access children)



class Project(SAFRSBaseX, Base):
    """
    description: Company projects, involving employees.
    """
    __tablename__ = 'projects'
    _s_collection_name = 'Project'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    budget = Column(Float)
    department_id = Column(ForeignKey('departments.id'))

    # parent relationships (access parent)
    department : Mapped["Department"] = relationship(back_populates=("ProjectList"))

    # child relationships (access children)



class Order(SAFRSBaseX, Base):
    """
    description: Customer orders of products.
    """
    __tablename__ = 'orders'
    _s_collection_name = 'Order'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    date_created = Column(DateTime)
    customer_id = Column(ForeignKey('customers.id'))
    employee_id = Column(ForeignKey('employees.id'))

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("OrderList"))
    employee : Mapped["Employee"] = relationship(back_populates=("OrderList"))

    # child relationships (access children)
    InvoiceList : Mapped[List["Invoice"]] = relationship(back_populates="order")
    ShipmentList : Mapped[List["Shipment"]] = relationship(back_populates="order")



class Invoice(SAFRSBaseX, Base):
    """
    description: Invoices issued for customer orders.
    """
    __tablename__ = 'invoices'
    _s_collection_name = 'Invoice'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey('orders.id'))
    total_amount = Column(Float, nullable=False)

    # parent relationships (access parent)
    order : Mapped["Order"] = relationship(back_populates=("InvoiceList"))

    # child relationships (access children)
    PaymentList : Mapped[List["Payment"]] = relationship(back_populates="invoice")



class Shipment(SAFRSBaseX, Base):
    """
    description: Shipments made for orders.
    """
    __tablename__ = 'shipments'
    _s_collection_name = 'Shipment'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey('orders.id'))
    shipped_date = Column(DateTime)

    # parent relationships (access parent)
    order : Mapped["Order"] = relationship(back_populates=("ShipmentList"))

    # child relationships (access children)



class Payment(SAFRSBaseX, Base):
    """
    description: Payments received from customers for orders.
    """
    __tablename__ = 'payments'
    _s_collection_name = 'Payment'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    invoice_id = Column(ForeignKey('invoices.id'))
    amount_paid = Column(Float, nullable=False)
    payment_date = Column(DateTime)

    # parent relationships (access parent)
    invoice : Mapped["Invoice"] = relationship(back_populates=("PaymentList"))

    # child relationships (access children)
