from interfaces.repositores import OrderRepository
from entities.order import Order,OrderModel
from entities.customer_persone import PersoneModel,Persone



class CustomerDB:
    def __init__(self) -> None:
        self.db = []
    def search(self,pk):
        data_db = [{1:{"name":"boubaker","phone":"06 63 36  69 15 ","balance":100}},
                   {2:{"name":"rachid","phone":"06 63 36  69 32 ","balance":130}}]
        
        for customer_dict in data_db:
            if pk in customer_dict:
                return customer_dict[pk]
        return f"cutsomer_id:{pk} not Exist!!"
        
            
    def save(self,customer:PersoneModel):
        check_db = self.check(customer.id)
        if check_db == False:
            return f"save customer:{customer.name}"
        else:
            return f"already exist:{customer.name}"

        

    def check(self,customer_id):
        result = self.search(customer_id)
        if result == f"cutsomer_id:{customer_id} not Exist!!":
            return False
        else:
            return True



        
 

class OrderDB:
    def __init__(self) -> None:
        pass

    def save(self,order:OrderModel):
        return {"order":order}


class StockDB:
    def __init__(self) -> None:
        pass
    def data_customer(self):
        customers = [
            {"id":1,"name":"Boubaker Elbikam","phone":"+212 6 63 36 69 15","balance":100
    
        }
        ]
        return customers
    
    
    def data_stock(self):
        stock = [
            {"id": 101, "name": "Laptop", "price": 999.99,"current_qte":10},
            {"id": 102, "name": "Smartphone", "price": 699.99,"current_qte":10}
        ]
        return stock
    def save(self,stock:OrderModel):
        return {"state":"successful","stock":stock}


        
        