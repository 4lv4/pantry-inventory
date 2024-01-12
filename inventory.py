class Ingredience:
    def __init__(self, type, unit, amount, tags = None, pantry_location = None, best_before = None, always_stock = False, limit = '1000'):
        self.type = type
        self.unit = unit
        self.amount = amount
        self.tags = tags
        self.pantry_location = pantry_location