from abc import ABC,abstractmethod
from entities.order import Order


class OrderRepository(ABC):
    @abstractmethod
    def save(self):
        pass


class GetCustomerRepository(ABC):
    @abstractmethod
    def get_info(self):
        pass