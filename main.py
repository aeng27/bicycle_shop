from bicycle import *

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