from core_business.use_cases.entities.customer_persone import Persone,PersoneModel

from interfaces.services import CreateCustomerService



class CreateCustomerUseCase:
    def __init__(self,service:CreateCustomerService) -> None:
        self.service = service



    def apply(self,customer:PersoneModel):
        return self.service.execute(customer)





