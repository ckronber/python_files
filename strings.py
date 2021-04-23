def substring_between_letters(word,start,end):
    if(word.find(start) >= 0 and word.find(end) >= 0):
        substr = word[word.find(start)+1:word.find(end)]
    else:
        return word
    return substr

#function that checks if words in a sentence are longer than integer x
def x_length_words(sentence,x):
    count = 0
    split = sentence.split()
    for word in split:
        if(len(word) >= x):
            count+=1
    if(count == len(split)):
        return True
    else:
        return False
        

#function that checks for a name in a sentence
def check_for_name(sentence,name):
    split = []
    count = 0
    name = name.lower()
    split = sentence.split()
    
    for word in split:
        word = word.lower()
        if(word == name):
            count += 1
            
    if(count >0):
        return True
    else:
        return False
        
#function that takes a word and prints out every other letter
def every_other_letter(word):
    string2 = ""
    for i in range(len(word)):
        if(i%2 == 0):
            string2 += word[i]
    return string2

#function that reverses a string
def reverse_string(word):
    str_reverse = ""
    count = len(word)-1
    for letter in word:
       str_reverse += word[count]
       count -= 1
    return str_reverse

def make_spoonerism(word1,word2):
    replaceLetter = ""
    replaceLetter2 = ""
    spoonerism = ""
    replaceLetter = word1[0]
    replaceLetter2 = word2[0]
    repword1 = replaceLetter2 + word1[1:]
    repword2 = replaceLetter + word2[1:]
    spoonerism = repword1 + " " + repword2
    return spoonerism
    
def add_exclamation(word):
    word2 = ""
    count = 0
    if(len(word) < 20):
        count = 20-len(word)
        for i in range(count):
            word2 += "!"
        return word+word2
    else:
        return word
        
def count_multi_char_x(word,x):
    count = 0
    new_word = []
    new_word = word
    count = new_word.count(x)
    return count
    
def count_char_x(word,x):
    count = 0
    for letter in word:
        if(letter == x):
            count += 1
        else:
            continue
    return count

def unique_english_letters(word):
  letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
  new_letters = letters
  unique = []
  for let in word:
      if(let in new_letters):
          unique.append(new_letters[new_letters.find(let)])
          new_letters = new_letters.replace(let,'')
  return len(unique)
  
#print(substring_between_letters("apple","p","c"))
#print(x_length_words("i likes apples", 2))
#print(check_for_name("my name is Jamie", "Jamie"))
#print(every_other_letter("Hello world!"))
#print(reverse_string("Codecademy"))
#print(make_spoonerism("Codecademy", "Learn"))
#print(make_spoonerism("Hello", "world!"))
#print(add_exclamation("Codecademy"))
#print(count_multi_char_x("mississippi","iss"))
#print(count_char_x("mississippi","s"))
#print(unique_english_letters("banana"))
#print(unique_english_letters("Apple"))