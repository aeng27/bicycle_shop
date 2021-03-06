class bicycle(object):
  def __init__(self, name, weight, production_cost):
      self.name = name
      self.weight = weight
      self.production_cost = production_cost

class bike_shop(object):
  def __init__(self, name, inventory, margin):
      self.name = name
      self.margin = margin
      self.inventory = inventory
      self.profit = []
      
  def price(self):
      self.price = {}
      for bike in self.inventory:
        self.price [bike.name] = bike.production_cost *((self.margin/100) + 1)
        
  def inventory_name(self):
      self.inventory_name = [bike.name for bike in self.inventory]
      return self.inventory_name
    
class customer(object):
  def __init__(self, name, budget):
      self.name = name
      self.budget = budget
  def afford(self, shop):
      self.buy = []
      for bike in shop.inventory_name:
        if self.budget > shop.price[bike]:
          self.buy.append(bike)
      print "{} can afford a {}".format(self.name,', '.join(self.buy))

class purchase(object):
  def __init__(self, name, bike, shop):
    self.name = name
    self.bike = bike
    self.shop = shop
    self.money_left = self.name.budget - self.shop.price[self.bike]
    print "{} bought a {} and has ${} left over.".format(self.name.name, self.bike, self.money_left)
    self.shop.profit.append(self.shop.price[self.bike])
    
class update_inventory(object):
  def __init__(self,bike,shop):
    self.bike = bike
    self.shop = shop
    self.shop.inventory[self.bike] = self.shop.inventory[self.bike] - 1

Starter_Bike = bicycle("Starter Bike", 30, 165)
Commuter_Bike = bicycle("Commuter Bike", 27, 200)
Mountain_Bike = bicycle("Mountain Bike", 30, 370)
Folding_Bike = bicycle("Folding Bike", 25, 415)
Racing_Bike = bicycle("Racing Bike", 24, 820)
Road_Bike = bicycle("Road Bike", 24, 830)

City_Bikes = bike_shop("City Bikes", {Starter_Bike: 3, Commuter_Bike: 3, Mountain_Bike:3, Folding_Bike:3, Racing_Bike:3, Road_Bike:3}, 20.0)
City_Bikes.price()
City_Bikes.inventory_name()
        
Emily = customer("Emily", 1000)
Katy = customer("Katy", 500)
Alyssa = customer("Alyssa", 250)
customers = [Emily, Katy, Alyssa]

print "These are the bikes we have in stock: {}".format(', '.join(City_Bikes.inventory_name))

print "Here is what each of our customers can afford:"
for customer in customers:
  customer.afford(City_Bikes)
  
purchase(Emily, "Racing Bike", City_Bikes)
purchase(Katy, "Folding Bike", City_Bikes)
purchase(Alyssa, "Commuter Bike", City_Bikes)

update_inventory(Racing_Bike, City_Bikes)
update_inventory(Folding_Bike, City_Bikes)
update_inventory(Commuter_Bike, City_Bikes)

print "The remaining inventory in City Bikes is:"

for bike in City_Bikes.inventory:
  print [bike.name, City_Bikes.inventory[bike]]
print "Our profit from bikes sold is ${}".format(sum(City_Bikes.profit))
