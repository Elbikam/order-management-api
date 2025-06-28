from abc import ABC,abstractmethod
from entities.order import Order,OrderModel
from entities.customer_persone import Persone,PersoneModel

class OrderRepository(ABC):
    @abstractmethod
    def check_avaibility(self,qte,item_id):
        pass
    @abstractmethod
    def tax(self,rate):
        pass
    @abstractmethod
    def subtoatl(self,item:Order):
        pass
    @abstractmethod
    def check_balance(self,customer_id):
        pass

class GetCustomerRepository(ABC):
    @abstractmethod
    def get_info(self):
        pass


class CreateCustomerRepository(ABC):
    @abstractmethod
    def execute(self,customer):
        pass