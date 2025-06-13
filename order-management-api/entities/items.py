

class Item:
    def __init__(self,item_id:str,item_name:str,description:str,price:float) -> None:
        self.item_id = item_id
        self.item_name = item_name
        self.description = description
        self.price = price

        