from interfaces.repositores import OrderRepository
from core_business.use_cases.entities.order import Order,OrderModel
from core_business.use_cases.entities.customer_persone import PersoneModel,Persone





class CustomerDB:
    def __init__(self) -> None:
        pass
    def execute(self,customer_id) -> PersoneModel:
        data = {"customer_id":customer_id,
                    "name":"boubaker","phone":"663366915"}
        return data 
    


    def save(self,customer:PersoneModel):
        return {"state":"success","customer":customer}


class OrderDB:
    def __init__(self) -> None:
        pass

    def save(self,order:OrderModel):
        return {"order":order}
