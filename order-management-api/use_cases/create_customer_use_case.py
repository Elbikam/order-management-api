from entities.customer_persone import Persone,PersoneModel
from interfaces.services import CreateCustomerService



class CreateCustomerUserCase:
    def __init__(self,
                 create_customer_service: CreateCustomerService):
        self.create_customer_service = create_customer_service
        
    def add_new_customer(self,customer:PersoneModel):
        result = self.create_customer_service.execute(customer)
        return result
    
