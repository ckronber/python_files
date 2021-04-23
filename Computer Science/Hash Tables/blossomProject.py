from linked_list import Node, LinkedList

class HashMap():
  def __init__(self,size):
    self.size = size
    self.array = [LinkedList()]*size
    print(self.array)

  def hash(self, key, count_collisions=0):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return (hash_code + count_collisions)%self.size

  def assign(self,key,value):
    array_index = self.hash(key)
    payload = Node([key,value])
    list_at_array = self.array[array_index]
    for key in list_at_array:
        if(key == list_at_array[0]):
            list_at_array[1] = value
        else:
            self.array[array_index] = payload
    
  def retrieve(self,key):
    array_index = self.hash(key)
    payload = self.array[array_index]
    if(payload[0] == key):
      return payload[1]
    else:
      return None
      
    #This is a function for printing the hash table
  def printTable(self):
    print(self.array)

hash = HashMap(10)
hash.assign('make','lunch')
