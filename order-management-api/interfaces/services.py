from data_base  import CustomerDB,OrderDB,StockDB
from interfaces.repositores import OrderRepository,GetCustomerRepository
from entities.customer_persone import Persone,PersoneModel
from entities.order import Order
from interfaces.repositores import CreateCustomerRepository

from entities.stock import Stock,StockModel



    


class CreateCustomerService(CreateCustomerRepository):
    def __init__(self,db:CustomerDB) -> None:
        self.db = db

    def execute(self, customer:PersoneModel):
        return self.db.save(customer) 

class CreateOrderService(OrderRepository):
    def __init__(self,db:StockDB) -> None:
        super().__init__()
        self.db = db
    def check_balance(self, customer_id:PersoneModel) -> bool:
        customers = self.db.data_customer()
        for b in customers:
            if b["id"] == customer_id:
                return True
        return False
    


    def check_avaibility(self, qte, item_id) -> bool:
        stock = self.db.data_stock()
        for item in stock:
            if item['id'] == item_id and item['current_qte'] >= qte:
                return True
        return False
        
    def tax(self,rate):
        return rate
    def subtoatl(self, order:Order):
        subtotal = order.price * order.qte
        return subtotal
    def save_order(self, order:Order):
        return self.db.save(order)
        
    

    

    
    