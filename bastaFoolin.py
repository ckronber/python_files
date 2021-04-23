class menu():
  def __init__(self,name,items,start_time,end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
    
  def __repr__(self):
    return self.name + " avaliable from " + self.start_time + " to " +self.end_time
    
  def calculate_bill(self,purchased_items):
    total = 0
    for key in self.items.keys():
      for item in purchased_items:
        if(item == key):
            total += self.items[key]
    return total
          
          
class Franchise():
  def __init__(self,address,menus):
    self.address = address
    self.menus = menus
    
  def __repr__(self):
    return self.address
    
  def avaliable_menus(self,time):
    menu = []
    if(time >= 11 and time <= 16):
      menu.append(self.menus[0])
    if(time >= 15 and time <= 18):
      menu.append(self.menus[1])
    if(time >= 17 and time <= 23):
      menu.append(self.menus[2])
    if(time >= 11 and time <= 21):
      menu.append(self.menus[3])
    return menu
    
brunch = menu("Brunch Menu",{'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50},"11am","4pm")

early_bird = menu("Early Bird Menu", {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
},"3pm","6pm")

dinner = menu("Dinner Menu",{
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
},"5pm","11pm")

kids = menu("Kids Menu", {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, "11am", "9pm")

arepas_menu = menu("Take a' Arepa", {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50},"10am","8pm")

print(brunch)
print(brunch.calculate_bill(['pancakes','home fries','coffee']))
print(early_bird.calculate_bill(['salumeria plate','mushroom ravioli (vegan)']))

flagship_store = Franchise("1232 West End Road",[brunch,early_bird,dinner,kids])
new_installment = Franchise("12 East Mulberry Street",[brunch,early_bird,dinner,kids])

print(flagship_store.avaliable_menus(17))

class Business():
  def __init__(self,name,franchises):
    self.name = name
    
start_business = Business("Basta Fazoolin' with my Heart",[flagship_store,new_installment])

arepas_place = Franchise("198 Fitzgerald Avenue", arepas_menu)

take_arepa = Business("Take a' Arepa",[arepas_place])