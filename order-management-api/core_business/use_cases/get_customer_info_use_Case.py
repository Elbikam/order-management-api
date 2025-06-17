from interfaces.services import GetInfo



class GetCustomerInfoUseCase:
    def __init__(self,getinfo:GetInfo) -> None:
        self.getinfo = getinfo

    def details_cuctomer(self,customer_id):
        return self.getinfo.get_info(customer_id)