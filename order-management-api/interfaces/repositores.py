from abc import ABC,abstractmethod
from core_business.use_cases.entities.order import Order,OrderModel
from core_business.use_cases.entities.customer_persone import Persone,PersoneModel

class OrderRepository(ABC):
    @abstractmethod
    def check_avaibility(self,qte,item):
        pass
    @abstractmethod
    def tax(self):
        pass
    @abstractmethod
    def subtoatl(self,item:Order):
        pass
    @abstractmethod
    def check_balance(self,customer:Persone):
        pass
        

class GetCustomerRepository(ABC):
    @abstractmethod
    def get_info(self):
        pass


class CreateCustomerRepository(ABC):
    @abstractmethod
    def execute(self,customer):
        pass