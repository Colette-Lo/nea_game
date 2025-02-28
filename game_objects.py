# Product class
class Product:
    def __init__(self, name, base, supply):
        self.name = name
        self.price = base
        self.supply = supply
        self.modifier = 1

        self.price_change()

    def price_change(self):
        self.price = self.price * (1+self.modifier)

    def adjust_modifier(self, change):
        self.modifier += change

# Good class
class Good(Product):
    def __init__(self, name, base, supply, base_demand):
        super().__init__(name, base, supply)
        self.name = name
        self.price = base
        self.supply = supply
        self.modifier = 1
        self.demand = base_demand
        self.sold = 0.0

    def demand_change(self, factor):
        self.demand = self.demand * (1+factor)

    def restock(self, add_supply):
        self.supply += add_supply

    def sold_change(self, factor):
        if self.supply < self.demand:
            self.sold = self.supply
        else:
            self.sold = self.demand

# Raw material class
class RawMaterial(Product):
    def __init__(self, name, base, supply):
        super().__init__(name, base, supply)
        self.name = name
        self.price = base
        self.supply = supply
        self.modifier = 1
        self.unit_cost = 0.0
        self.ex_cost = 0.0

    def update_ex_cost(self, add_quantity):
        additional = add_quantity
        new_cost = self.unit_cost * additional
        self.ex_cost = new_cost
        return new_cost

# create objects


# Raw materials: coal, oil, crops, metals, timber, wool
coal = RawMaterial(name='Coal', base=100, supply=100)
oil = RawMaterial(name='Oil', base=100, supply=100)
crops = RawMaterial(name='Crops', base=100, supply=100)
metals = RawMaterial(name='Metals', base=100, supply=100)
timber = RawMaterial(name='Timber', base=100, supply=100)
wool = RawMaterial(name='Wool', base=100, supply=100)