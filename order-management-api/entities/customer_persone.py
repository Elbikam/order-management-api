from abc import ABC,abstractmethod

from pydantic import BaseModel # type: ignore


class Persone(object):
    def __init__(self,id,name,phone,balance=None) -> None:
        self.id = id
        self.name = name
        self.phone = phone
        self.balance = None
        


    def customer_info(self):
        return    self.name + '|'+ self.phone
    

class PersoneModel(BaseModel):
    id : int
    name : str
    phone : str 
    balance : float
