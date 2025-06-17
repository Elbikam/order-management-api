from abc import ABC,abstractmethod

from pydantic import BaseModel


class Persone(object):
    def __init__(self,customer_id,name,phone) -> None:
        self.customer_id = customer_id
        self.name = name
        self.phone = phone

    def customer_info(self):
        return    self.name + '|'+ self.phone
    

class PersoneModel(BaseModel):
    customer_id : int
    name : str
    phone : str 
