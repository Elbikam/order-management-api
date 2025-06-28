from entities.stock import Stock,StockModel

from pydantic import BaseModel # type: ignore
from entities.customer_persone import Persone,PersoneModel

class OrderModel(BaseModel):
    id : int
    item_di : int
    description : str
    price : float 
    qte : int







class Order(object):
    def __init__(self,id,item_id,description,price,qte) -> None:
        self.id = id
        self.item_id = item_id
        self.description = description
        self.price = price
        self.qte = qte

    def sub_total(self,order:OrderModel):
        total = self.price*self.qte
        return total
    

