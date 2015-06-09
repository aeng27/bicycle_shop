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