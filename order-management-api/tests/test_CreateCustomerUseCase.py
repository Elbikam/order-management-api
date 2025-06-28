from interfaces.repositores import CreateCustomerRepository
from interfaces.services import CreateCustomerService
from entities.customer_persone import Persone,PersoneModel
from unittest import mock  
from use_cases.create_customer_use_case import CreateCustomerUserCase

from data_base import CustomerDB

def test_create_customer():
    db = CustomerDB()
    s = CreateCustomerService(db)
    c = CreateCustomerUserCase(s)
    p = PersoneModel(id=1,name="Boubaker Elbikam",phone="+212 6 76 824202",balance=90)
    response = c.add_new_customer(p)
    assert response == f"already exist:{p.name}"
    

    
    

    
    
