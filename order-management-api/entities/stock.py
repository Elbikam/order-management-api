
from entities.items import Item

class Stock:

    listSTock = []
    def add_to_stock(self,item:Item,qte:int):
        product = {'id':item.item_id,'qte':qte}
        self.listSTock.append(product)
        return self.listSTock