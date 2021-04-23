# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

def censor(phrase):
  email_one_replace = email_one.replace(phrase, "CENSORED!")
  return email_one_replace

#print(censor("learning algorithms"))

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

email_two_replace = email_two.lower()
email_two_replace = email_two_replace.split()

print(email_two_replace)

def censor_list(lists):
  for i in range(len(email_two_replace)):
    for j in range(len)
    
  return email_two_replace

print(censor_list(proprietary_terms))
