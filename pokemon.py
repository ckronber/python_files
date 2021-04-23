#,level,poke_type,max_health,current_health,ko
class Pokemon:
  def __init__(self,name):
    self.name = name[0]
    self.level =name[1] 
    self.poke_type = name[2]
    self.max_health = name[3]
    self.current_health = name[4]
    self.ko = name[5]
  
  def __repr__(self):
      return "{name} is a {level} level {ptype} Pokemon with a current health of {curr_health}".format(name = self.name, level = self.level,ptype =self.poke_type, curr_health = self.current_health)
  
  def lose_health(self,damage):
    health = 0
    print("{name} has taken {damage} damage".format(name = self.name, damage = damage))
    health = self.current_health - damage
    
    if(health > 0):
      self.current_health = health
      print("{} is now at {} Health".format(self.name, health))
    else:
      self.current_health = 0
      self.ko = True
      print("{name} has been knocked out!").format(name = self.name)
    
  def regain_health(self, healing):
    if((healing + self.current_health) > self.max_health):
      self.current_health = self.max_health
      print("{} is already at max health".format(self.name))
   
    else:
      regain = self.current_health + healing
      self.current_health = regain
      print("{} has gained {} health".format(self.name, healing))
      
    print("{name} now has {chealth} health".format(name = self.name, chealth = self.current_health))
    
#  def attack(other_pokemon):

#This is an easier way to create a pokedex with all of the pokemon used here
Pokedex = {"Charizard":["Charizard",100,"Fire",10000,10000,False],"Squirtle":["Squirtle",100,"Fire",1800,2000,False]}
print(Pokedex.keys())
Charizard = Pokemon(Pokedex["Charizard"])
Squirtle = Pokemon(Pokedex["Squirtle"])

print(Charizard)