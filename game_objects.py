# Product class
from sys import intern

from object_dictionaries import materials


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
    def __init__(self, name, base, supply, base_demand, tech):
        super().__init__(name, base, supply)
        self.name = name
        self.price = base
        self.supply = supply
        self.modifier = 1
        self.demand = base_demand
        self.sold = 0.0
        self.related_tech = tech

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
    def __init__(self, name, base, supply, extract_time):
        super().__init__(name, base, supply)
        self.name = name
        self.price = base
        self.supply = supply
        self.modifier = 0.0
        self.unit_cost = 0.0
        self.ex_cost = 0.0
        self.operation_time = extract_time


    def update_ex_cost(self, add_quantity):
        additional = add_quantity
        new_cost = self.unit_cost * additional
        self.ex_cost = new_cost
        return new_cost

# create objects

# Raw materials: coal, oil, crops, metals, timber, wool
coal = RawMaterial(name='Coal', base=100, supply=100, extract_time=materials["Coal"]["operation_time"])
oil = RawMaterial(name='Oil', base=100, supply=100, extract_time=materials["Oil"]["operation_time"])
crops = RawMaterial(name='Crops', base=100, supply=100, extract_time=materials["Crops"]["operation_time"])
metals = RawMaterial(name='Metals', base=100, supply=100, extract_time=materials["Metals"]["operation_time"])
timber = RawMaterial(name='Timber', base=100, supply=100, extract_time=materials["Timber"]["operation_time"])
wool = RawMaterial(name='Wool', base=100, supply=100, extract_time=materials["Wool"]["operation_time"])


# Goods: Food, clothing, electronics, medicines, vehicles, books, furniture, hygiene products, internet, household appliances
food = Good(name='Food', base=100, supply=100, base_demand=100000, tech="mech")
clothing = Good(name="Clothing", base=100, supply=100, base_demand=100000, tech="mech")
electronics = Good(name='Electronics', base=100, supply=100, base_demand=100000, tech="chem&power")
medicines = Good(name='Medicines', base=100, supply=100, base_demand=100000, tech="chem&power")
vehicles = Good(name='Vehicles', base=100, supply=100, base_demand=100000, tech="electricity")
books = Good(name='Books', base=100, supply=100, base_demand=100000, tech="mech")
furniture = Good(name='Furniture', base=100, supply=100, base_demand=100000, tech="mech")
hygiene = Good(name='Hygiene products', base=100, supply=100, base_demand=100000, tech="chem&power")
internet = Good(name='Internet', base=100, supply=100, base_demand=100000, tech="electricity")
house_appliances = Good(name='Household appliances', base=100, supply=100, base_demand=100000, tech="electricity")

good_list = [food, clothing, electronics, medicines, vehicles, books, furniture, hygiene, internet, house_appliances]
prices = [food.price, clothing.price, electronics.price, medicines.price, vehicles.price, books.price, furniture.price, hygiene.price, internet.price, house_appliances.price]
quantity_sold = [food.sold, clothing.sold, electronics.sold, medicines.sold, vehicles.sold, books.sold, furniture.sold, hygiene.sold, internet.sold, house_appliances.sold]