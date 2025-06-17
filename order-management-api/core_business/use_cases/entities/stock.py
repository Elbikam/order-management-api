from pydantic import BaseModel
from core_business.use_cases.entities.items import Item,ItemModel


class Stock(object):
    def __init__(self,items:Item) -> None:
        self.items = [items]


    def add(self,products):
        self.items.append(products)



class StockModel(BaseModel):
    items : list[ItemModel]