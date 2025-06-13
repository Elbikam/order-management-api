from .customer_abs import Customer

class Company(Customer):
    def __init__(self,company_name:str,ice:str) -> None:
        super().__init__()
        self.company_name = company_name
        self.ice= ice

    def customer_info(self):
        return self.company_name +'|'+self.ice    