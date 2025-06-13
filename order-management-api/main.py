from fastapi import FastAPI
from frameworks.db.postgres import CustomerDB
from entities.customer_persone import Persone
from interfaces.services import GetInfo
import logging
from use_cases.get_customer_info_use_Case import GetCustomerInfoUseCase
logger = logging.getLogger(__name__)

app = FastAPI()

db = CustomerDB
getinfo = GetInfo(db)



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/customer/{customer_id}")
def get_info(customer_id: int) -> dict:
    "Proved information of customer"
    logger.info(
        "Getting customer info:%s",customer_id

    )
    customer = GetCustomerInfoUseCase(getinfo)
    details=  customer.details_cuctomer(customer_id)
    return {"customer_id": details}

