from entities import stock,order
from interfaces.services import CreateOrderService
from entities.customer_persone import PersoneModel,Persone
from entities.stock import StockModel,Stock

from entities.order import OrderModel,Order


class PlaceOrder(object):
    def __init__(self,customer:Persone,order:Order,service:CreateOrderService) -> None:
        self.customer = customer
        self.order = order
        self.service = service
       

    def execute_order(self):
        customer_balance = self.service.check_balance(self.customer.id)
        check_first_item = self.service.check_avaibility(self.order.qte,self.order.item_id)
        if not check_first_item:
            return {"status":"error","message":"Item not available in stock"}                           
        if check_first_item:
            total = self.service.subtoatl(self.order)
            if customer_balance <= total:
                self.service.save_order(self.order)
                return {"status":"success","message":"Order placed successfully","order":self.order.id,"sub_total":total}
            else:
                return {"status":"you extend your Balance ."}
        

        



    