from unittest import mock  
from fastapi.testclient import TestClient 
from main import app
from entities.customer_persone import Persone, PersoneModel
from fastapi import FastAPI  # type: ignore

import pytest




client = TestClient(app)

def test_create_customer():
    persone = PersoneModel(id=5, name="John Doe", phone="1234567890",balance=100.0)
    response = client.post("/create_new_customer/", json =persone.model_dump())
   
    # assert response.json()== f"already exist:{persone.name}"
    assert response.json() == f"save customer:{persone.name}"
   
    
    



        
            
            
           
        

   
        

        
    
    
   
   
 
                                      