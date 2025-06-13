
from abc import ABC,abstractmethod
from .customer_abs import Customer

class Persone(Customer):
    def __init__(self,name,phone) -> None:
        super().__init__()
        self.name = name
        self.phone = phone 
    def customer_info(self):
        return    self.name + '|'+ self.phone
    
