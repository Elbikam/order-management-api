from pydantic import BaseModel # type: ignore



class Stock(object):
    def __init__(self,id,brand,description,current_qte) -> None:
        self.id = id 
        self.brand = brand
        self.description = description
        self.current_qte = current_qte



    


class StockModel(BaseModel):
    id :int
    brand : str
    description : str
    current_qte : int
