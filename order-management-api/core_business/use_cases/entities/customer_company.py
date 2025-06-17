from pydantic import BaseModel


class Company(object):
    def __init__(self,company_id,company_name,ice) -> None:
        self.company_id = company_id
        self.company_name = company_name
        self.ice = ice 

    def customer_info(self):
        return self.company_name +'|'+self.ice 

class CompanyModel(BaseModel):
    company_id : int
    company_name :str
    ice : str
