from data_base  import CustomerDB,OrderDB
from interfaces.repositores import OrderRepository,GetCustomerRepository
from core_business.use_cases.entities.customer_persone import Persone,PersoneModel
from core_business.use_cases.entities.order import Order
from interfaces.repositores import CreateCustomerRepository
from core_business.use_cases.entities.items import ItemModel,Item
from core_business.use_cases.entities.stock import Stock,StockModel


class GetInfo(GetCustomerRepository):
    def __init__(self,customer_id:CustomerDB) -> None:
        super().__init__()
        self.customer_id  = customer_id


    def get_info(self,customer_id):
        
        customer = self.customer_id.execute(customer_id)

        return customer
    


class CreateCustomerService(CreateCustomerRepository):
    def __init__(self,db:CustomerDB) -> None:
        self.db = db



    def execute(self, customer:PersoneModel):
        return self.db.save(customer) 

class CreateOrderService(OrderRepository):
    def __init__(self,db:OrderDB) -> None:
        super().__init__()
        self.db = db

    def check_avaibility(self, qte:int, item:ItemModel) -> bool:
        if item in StockModel.items and qte <= item.item_qte:
            return True
        else:
            return False
    def tax(self):
        return .2
    def subtoatl(self, items: Stock):
        subtotal = 0
        pass
            

    

    
    