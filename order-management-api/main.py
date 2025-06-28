from fastapi import FastAPI # type: ignore
from data_base import CustomerDB, StockDB
from interfaces.services import CustomerDB, StockDB

import logging

from entities.customer_persone import Persone,PersoneModel
from interfaces.services import CreateCustomerService
from entities.stock import Stock,StockModel
from use_cases.create_customer_use_case import CreateCustomerUserCase
from use_cases.place_order import PlaceOrder
from entities.order import Order,OrderModel
from interfaces.services import CreateOrderService
logger = logging.getLogger(__name__)

app = FastAPI()


# dependency injection 
db = CustomerDB()


cr=CreateCustomerService(db)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/customer/{customer_id}")
def get_info(customer_id) ->PersoneModel:
    pass

@app.post("/create_new_customer/")
async def create_new_customer(customer:PersoneModel):
    """
    Create a new customer.
    """
    create_customer_use_case = CreateCustomerUserCase(cr)
    result = create_customer_use_case.add_new_customer(customer)
    return result
    
  
    


db_s = StockDB()



@app.post("/create_order")
def place_order(order:OrderModel,customer:PersoneModel):
    pass