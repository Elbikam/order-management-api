from fastapi import FastAPI
from data_base import CustomerDB
from interfaces.services import GetInfo
import logging
from core_business.use_cases.get_customer_info_use_Case import GetCustomerInfoUseCase
from core_business.use_cases.create_customer_use_case import CreateCustomerUseCase
from core_business.use_cases.entities.customer_persone import Persone,PersoneModel
from interfaces.services import CreateCustomerService
logger = logging.getLogger(__name__)

app = FastAPI()


# dependency injection 
db = CustomerDB()
getinfo = GetInfo(db)

cr=CreateCustomerService(db)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/customer/{customer_id}")
def get_info(customer_id) ->PersoneModel:
    "Proved information of customer"
    logger.info(
        "Getting customer info:%s",customer_id

    )
    customer = GetCustomerInfoUseCase(getinfo)
    details=  customer.details_cuctomer(customer_id)
    return details

@app.post("/customer")
def create_customer(customer: PersoneModel):
    "Create a new customer"
    logger.info("Creating new customer")
    create_it = CreateCustomerUseCase(cr)
    return {"message": "Customer created successfully", "customer":create_it.apply(customer)}

