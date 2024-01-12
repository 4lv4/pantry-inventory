class Ingredience:
    #Initializing all the variables to keep track of
    def __init__(self, name, foodtype, unit, amount, nutrition = None, tags = None, pantry_location = None, best_before = None, always_stock = False, limit = '1000', ready_to_eat = False, preptime = None):
        self._info = {'name': name, 'foodtype': foodtype, 'unit':unit, 'amount': amount, 'nutrition': nutrition,'tags': tags, 'pantry_location': pantry_location, 
                      'best_before': best_before, 'always_stock': always_stock, 'limit': limit, 'ready_to_eat': ready_to_eat, 'preptime': preptime}
    #Getters
    def get_info(self):
        return self._info
    
    #Setters, not to be used directly. Only use in other function since we also need to update the Json file!
    def set_any(self, type, item):
        self._info[type] = item

    def set_name(self, name):
        self._info['name'] = name
    
    def set_foodtype(self, foodtype):
        self._info['foodtype'] = foodtype

    def set_unit(self, unit):
        self._info['unit'] = unit

    def set_amount(self, amount):
        self._info['amount'] = int(amount)

    def update_amount(self, amount):
        self._info['amount'] += int(amount)

    def set_nutrition(self, nutrition):
        self._info['nutrition'] = list(nutrition)

    def set_tags(self, tags):
        self._info['tags'] = set(tags)

    def update_tags(self, tags):
        self._info['tags'].add(tags)

    def set_pantry_location(self, pantry_location):
        self._info['pantry_location'] = pantry_location

    def set_best_before(self, best_before):
        self._info['best_before'] = best_before

    def set_always_stock(self, always_stock):
        self._info['always_stock'] = always_stock

    def set_limit(self, limit):
        self._info['limit'] = limit

    def set_ready_to_eat(self, ready_to_eat):
        self._info['ready_to_eat'] = ready_to_eat

    def set_prep_time(self, preptime):
        self._info['preptime'] = preptime


    
    