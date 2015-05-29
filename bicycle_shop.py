class bicycle(object):
  def __init__(self, name, weight, production_cost):
      self.name = name
      self.weight = weight
      self.production_cost = production_cost

Starter_Bike = bicycle("Starter Bike", 30, 165)
Commuter_Bike = bicycle("Commuter Bike", 27, 200)
Sport_Bike = bicycle("Sport Bike", 27, 290)
Mountain_Bike = bicycle("Mountain Bike", 30, 370)
Folding_Bike = bicycle("Folding Bike", 25, 415)
Road_Bike = bicycle("Road Bike", 26, 620)
Racing_Bike = bicycle("Racing Bike", 24, 820)
Specialized_Bike = bicycle("Specialized Bike", 24, 830)

class bike_shop(object):
  def __init__(self, name, inventory, margin):
      self.name = name
      self.inventory = inventory
      self.margin = margin
      
  def price(self):
      self.price = {}
      for bike in self.inventory:
        self.price [bike.name] = bike.production_cost *((self.margin/100) + 1)
        
cb_inventory = [Starter_Bike, Commuter_Bike, Mountain_Bike, Folding_Bike, Racing_Bike, Specialized_Bike]
City_Bikes = bike_shop("City Bikes", cb_inventory, 20.0)
City_Bikes.price()

class customer(object):
  def __init__(self, name, budget):
      self.name = name
      self.budget = budget
  def afford(self, shop):
      self.buy = [self.name]
      for bike in shop.price:
        if self.budget > shop.price[bike]:
          self.buy.append(bike)
        
Emily = customer("Emily", 1000)
Katy = customer("Katy", 500)
Alyssa = customer("Alyssa", 250)
customers = [Emily, Katy, Alyssa]
for customer in customers:
  customer.afford(City_Bikes)
  print customer.buy
