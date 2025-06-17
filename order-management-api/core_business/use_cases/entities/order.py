from core_business.use_cases.entities.stock import Stock,StockModel
from core_business.use_cases.entities.items import Item, ItemModel
from pydantic import BaseModel
from core_business.use_cases.entities.customer_persone import Persone,PersoneModel


class Order(object):
    def __init__(self,items:Stock,customer:Persone) -> None:
        self.items = items 
        self.customer = customer
    
    

class OrderModel(BaseModel):
    items : list[StockModel]
    customer : PersoneModel

