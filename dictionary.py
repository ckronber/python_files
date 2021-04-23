sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6 , "garage": 2 ,"driveway": 1}

#print(num_cameras)

#Create a dictionary from english to Sindarin
english_to_sindarin = {"mountain":"orod","bread":"bass","friend":"mellon","horse":"roch"}

#print(english_to_sindarin)

children = { "von Trapp":["Johannes", "Rosmarie", "Eleonore"], "Corleone" : ["Sonny", "Fredo", "Michael"]}
#print(children)

my_empty_dictionary = {}

animals_in_zoo = {}
animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurs"] = 0

#print(animals_in_zoo)

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}

user_ids.update({"theLooper":138475,"stringQueen":85739})

#print(user_ids)

oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

oscar_winners["Supporting Actress"] = "Viola Davis"
oscar_winners["Best Picture"] = "Moonlight"

#print(oscar_winners)

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks,caffeine)

drinks_to_caffeine = {}

for i in range(len(drinks)):
  drinks_to_caffeine[drinks[i]] = caffeine[i]

#print(drinks_to_caffeine)


songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {}

zipSongs = zip(songs,playcounts)

for i in range(len(songs)):
    plays[songs[i]] = playcounts[i]
 
#print(plays)

plays["Purple Haze"] = 1
plays["Respect"] = 94

#print(plays)
library = {"The Best Songs": plays,"Sunday Feelings":{}}

#print(library)

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
zodiac_elements["energy"] = "Not a Zodiac element"

#print(zodiac_elements["energy"])
#print(zodiac_elements["earth"])
#print(zodiac_elements["fire"])

caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}
caffeine_level["matcha"] = 30

#try:
  #print(caffeine_level["matcha"])
#except:
  #print("Unknown Caffeine Level")
  
  
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get("teraCoder", 100000)
#print(tc_id)

stack_id = user_ids.get("superStackSmash",100000)
#print(stack_id)


available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop("stamina grains",0)
#print(health_points)
health_points += available_items.pop("power stew",0)
#print(health_points)
health_points += available_items.pop("mystic bread",0)
#print(available_items)
#print(health_points)

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()
lessons = num_exercises.keys()

#print(users)

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0

for exercise in num_exercises:
  total_exercises += num_exercises[exercise]
  
#print(total_exercises)

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

#for occupation,pct in pct_women_in_occupation.items():
  #print("Women make up " + str(pct) + " percent of " + occupation +"s")
  
tarot = {1: "The Magician", 2: "The High Priestess", 3: "The Empress", 4: "The Emperor", 5: "The Hierophant", 6: "The Lovers", 7: "The Chariot", 8: "Strength", 9: "The Hermit", 10: "Wheel of Fortune", 11:	"Justice", 12: "The Hanged Man", 13: "Death", 14:	"Temperance", 15:	"The Devil", 16: "The Tower", 17: "The Star", 18:	"The Moon", 19:	"The Sun", 20: "Judgement", 21: "The World", 22: "The Fool"}

spread = {}
spread["past"] = tarot.pop(13)
spread["present"] = tarot.pop(22)
spread["future"] = tarot.pop(10)

#for key,value in spread.items():
  #print("Your " + key + " is the " + value + " card.")
  
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {letters:points for letters,points in zip(letters,points)}

letter_to_points[""] = 0

def score_word(word):
  point_total = 0
  
  try:
    for letter in word:
      point_total += letter_to_points[letter.upper()]
  except:
      point_total += 0
      
  return point_total
  
player_to_words = {"player1":["BLUE","TENNIS","EXIT"],"wordNerd":["EARTH","EYES","MACHINE"],"Lexi Con":["ERASER","BELLY","HUSKY"],"Prof Reader":["ZAP","COMA","PERIOD"]}
player_to_points =  {}

def update_points_totals():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points
  return print("Player Score Updated")
  
def play_word(player,word):
  list1 = []
  list1 = player_to_words[player]
  list1.append(word)
  player_to_words[player] = list1
  update_points_totals()
  return print(word + " added to " + player + " words.")
  
#play_word("player1","Booger")
#play_word("wordNerd","Earthquake")
#print(player_to_words)
#print(player_to_points)

def sum_values(my_dictionary):
  sumValues = 0
  for value1 in my_dictionary.values():
    sumValues += value1
  return sumValues

#print(sum_values({"milk":5, "eggs":2, "flour": 3}))

def sum_even_keys(my_dictionary):
  sumValues = 0
  for key,value1 in my_dictionary.items():
    if(key %2 == 0):
      sumValues += value1
  return sumValues
  
#print(sum_even_keys({1:5, 2:2, 3:3}))
#print(sum_even_keys({10:1, 100:2, 1000:3}))

def add_ten(my_dictionary):
  for key,value1 in my_dictionary.items():
    my_dictionary[key] = value1+10
  return my_dictionary
  
#print(add_ten({1:5, 2:2, 3:3}))

def values_that_are_keys(my_dictionary):
  list1 = []
  for key in my_dictionary.keys():
    for value in my_dictionary.values():
      if(value == key):
        list1.append(key)
  return list1
  
#print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
#print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))

def max_key(my_dictionary):
  max_val = 0
  for key,value1 in my_dictionary.items():
    if(value1 > max_val):
      max_val = value1
  
  for key in my_dictionary.keys():
    if(my_dictionary[key] == max_val):
      return key

#print(max_key({1:100, 2:1, 3:4, 4:10}))
#print(max_key({"a":100, "b":10, "c":1000}))

def word_length_dictionary(words):
  key = ""
  value = 0
  my_dictionary = {}
  
  for word in words:
    key = word
    value = len(word)
    my_dictionary[key] = value
  
  return my_dictionary
  
#print(word_length_dictionary(["apple", "dog", "cat"]))
#print(word_length_dictionary(["a", ""]))

def frequency_dictionary(words):
  my_dictionary = {}
  for word in words:
    try:
      if(my_dictionary[word]):
        my_dictionary[word] += 1
    except:
      my_dictionary[word] = 1
      
  return my_dictionary
  
#print(frequency_dictionary(["apple", "apple", "cat", 1]))
#print(frequency_dictionary([0,0,0,0,0]))

def unique_values(my_dictionary):
  sums = 0
  string1 = ""
  for value in my_dictionary.values():
    if(string1.find(str(value)) == -1):
      sums+=1
      string1 += str(value)
  return sums

#print(unique_values({0:3, 1:1, 4:1, 5:3}))
#print(unique_values({0:3, 1:3, 4:3, 5:3}))

def count_first_letter(names):
  new_dict = {}
  for key in names.keys():
    if(new_dict.get(key[0], -1) != -1):
      new_dict[key[0]] += len(names[key])
    else:
      new_dict[key[0]] = len(names[key])
  return new_dict
  
#print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
#print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))

