from unittest import mock  
from entities.customer_persone import Persone, PersoneModel
from fastapi import FastAPI  # type: ignore
import pytest
from data_base import CustomerDB

def test_search_customer_db():
    customer_id = 1
    db = CustomerDB()

    # with pytest.raises(ValueError):
    #    db.search(customer_id)
    response = db.search(customer_id)   
    assert response == {"name":"boubaker","phone":"06 63 36  69 15 ","balance":100}
    # assert response == 'cutsomer_id:13 not Exist!!'
    

def test_save_db():

    c = CustomerDB()
    p = PersoneModel(id=4,name="John",phone="+121 2273683",balance =2432)
    res = c.save(p)
    assert res == 'save customer:4'
    
def test_check_db():
    c = CustomerDB()
    p = PersoneModel(id=3,name="John",phone="+121 2273683",balance =2432)
    res = c.check(p)
    assert res == False