class bicycle(object):
  def __init__(self, name, weight, production_cost):
      self.name = name
      self.weight = weight
      self.production_cost = production_cost

Starter_Bike = bicycle("Starter Bike", 30, 125)
Commuter_Bike = bicycle("Commuter Bike", 27, 200)
Sport_Bike = bicycle("Sport Bike", 27, 350)
Mountain_Bike = bicycle("Mountain Bike", 30, 450)
Folding_Bike = bicycle("Folding Bike", 25, 500)
Road_Bike = bicycle("Road Bike", 26, 750)
Racing_Bike = bicycle("Racing Bike", 24, 1000)
Specialized_Bike = bicycle("Specialized Bike", 24, 1000)

class bike_shop(object):
  def __init__(self, name, inventory, margin):
      self.name = name
      self.inventory = inventory
      self.margin = margin
  def price(self, bike):
      self.price = self.production_cost * ((self.margin/100) + 1)
      

cb_inventory = [Starter_Bike, Commuter_Bike, Sport_Bike, Mountain_Bike, Folding_Bike, Road_Bike, Racing_Bike, Specialized_Bike]
City_Bikes = bike_shop("City Bikes", cb_inventory, 20)

class customer(object):
  def __init__(self, name, budget):
      self.name = name
      self.budget = budget

Emily = customer("Emily", 1000)
Katy = customer("Katy", 500)
Alyssa = customer("Alyssa", 250)

      