from interfaces.repositores import OrderRepository
from entities.order import Order
from entities.customer_persone import Persone





class CustomerDB:
    def __init__(self,customer:Persone) -> None:
        pass
    
    
    def execute(self,customer_id):
        return f"save succes:{customer_id}"   