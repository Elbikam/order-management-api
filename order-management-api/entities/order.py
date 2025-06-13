from entities.stock import Stock




class Order:
    def __init__(self, total: float, items: list[str]):
        self.total = total
        self.items = items

    def is_valid(self) -> bool:
        # Business rule: Order must have items and a positive total
        return self.total > 0 and len(self.items) > 0
