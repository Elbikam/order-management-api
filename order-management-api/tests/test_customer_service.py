from unittest import mock  
from entities.customer_persone import Persone, PersoneModel
from fastapi import FastAPI  # type: ignore
from interfaces.services import CreateCustomerService,CreateCustomerRepository
import pytest
from data_base import CustomerDB

def test_create_customer_service():
    db = CustomerDB()
    c = CreateCustomerService(db)
    customer = PersoneModel(id=2,name="boubaker",phone="06 63 36  69 15 ",balance=100)

    response = c.execute(customer)
    assert response == f"already exist:{customer.name}"
    # assert response == f"save customer:{customer.name}"

