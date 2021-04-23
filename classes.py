class Facade:
    pass

class Grade:
  minimum_passing = 65

class Circle:
  pi = 3.14
  # Add constructor here:
  def __init__(self,diameter):
    print("New circle with diameter: " + str(diameter))
    # Add assignment for self.radius here:
    self.radius = diameter/2
    pass
  def __repr__(self):
    return "Circle with radius {radius}".format(radius = self.radius)
  def area(self,radius):
    return self.pi*radius**2
  def circumference(self):
    return 2*self.pi*self.radius
 
class Rules:
 def washing_brushes(self):
    return "Point bristles towards the basin while washing your brushes."

facade_1 = Facade()
facade_1_type = type(facade_1)
print(facade_1_type)

circle = Circle(10)
pizza_area = circle.area(6)
teaching_table_area = circle.area(18)
round_room_area = circle.area(5730)

print(round_room_area)


class Store:
  pass

alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle\'s Ices"

print(isabelles_ices.store_name)


how_many_s = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in how_many_s:
  if hasattr(element,"count"):
    sum = element.count('s')
    print(sum)
    
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

print(medium_pizza)
print(teaching_table)
print(round_room)
