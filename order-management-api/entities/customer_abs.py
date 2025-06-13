from abc import ABC,abstractmethod

class Customer(ABC):
    
    @abstractmethod
    def customer_info(self):
        pass