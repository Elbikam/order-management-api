from frameworks.db.postgres import PostgresDB
from .repositores import OrderRepository,GetCustomerRepository
from entities.customer_persone import Persone
from entities.order import Order


class MockOrderRepository(OrderRepository):
    def __init__(self,db:PostgresDB) -> None:
        super().__init__()
        self.db = db
    
    def save(self):
        return self.db.execute()


class GetInfo(GetCustomerRepository):
    def __init__(self,customer_id:PostgresDB) -> None:
        super().__init__()
        self.customer_id  = customer_id


    def get_info(self,customer_id) -> dict:
        
        return {"customer_id":customer_id,"name":"boubaker","phone":"0663366915"} 

    