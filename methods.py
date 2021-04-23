class Message:
  def __init__(self, sender, recipient, text):
    self.sender = sender
    self.recipient = recipient
    self.text = text

class User:
  def __init__(self, username):
    self.username = username

  def edit_message(self, message, new_text):
    if message.sender == self.username:
      message.text = new_text

class Admin(User):
  def __init__(self,username):
    username = self.username = "Admin"
  
  def edit_message(self,message,new_text):
    message.text = new_text
    
    
class PotatoSalad:
  def __init__(self, potatoes, celery, onions):
    self.potatoes = potatoes
    self.celery = celery
    self.onions = onions

class SpecialPotatoSalad(PotatoSalad):
  def __init__(self,potatoes, celery, onions, raisins = 0):
    super().__init__(potatoes, celery, onions)
    self.raisins = 40
    
class InsurancePolicy:
  def __init__(self, price_of_item):
    self.price_of_insured_item = price_of_item

class VehicleInsurance(InsurancePolicy):
  def get_rate(self):
    return .001 * self.price_of_insured_item

class HomeInsurance(InsurancePolicy):
  def get_rate(self):
    return .00005* self.price_of_insured_item
    

class Atom:
  def __init__(self, label):
    self.label = label
  def __add__(self,other):
    return Molecule([self,other])

class Molecule:
  def __init__(self, atoms):
    if type(atoms) is list:
	    self.atoms = atoms

sodium = Atom("Na")
chlorine = Atom("Cl")
salt = Molecule([sodium, chlorine])
# salt = sodium + chlorine

class LawFirm:
  def __init__(self, practice, lawyers):
    self.practice = practice
    self.lawyers = lawyers
  
  def __len__(self):
    return len(self.lawyers)

  def __contains__(self,lawyer):
    if(self.lawyers.count(lawyer) >= 0):
      return lawyer
    else:
      return "Not a Lawyer"
      
   #def __contains__(self, lawyer):
    #return lawyer in self.lawyers

#d_and_p = LawFirm("Injury", ["Donelli", "Paderewski"])

class SortedList(list):
  def append(self, value):
    super().append(value)
    self.sort()

list = SortedList([1,4,3,2])
list.append(3)
#print(list)


class menu():
  def __init__(self,name,items,start_time,end_time):


