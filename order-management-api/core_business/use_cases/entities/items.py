from pydantic import BaseModel


class Item(object):
    def __init__(self,item_id,item_name,decription,price,item_qte) -> None:
        self.item_id = item_id
        self.item_name = item_name
        self.decription = decription
        self.price = price
        self.item_qte = item_qte



   
class ItemModel(BaseModel):
    item_id : str
    item_name : str
    description : str
    price : float    
    item_qte : int   