import re

#phoneNumRegex = re.compile(r'\d\d\d(-|.)\d\d\d(-|.)\d\d\d\d')
#phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d | \d\d\d.\d\d\d.\d\d\d\d') #works for findall with more than one type of phone number
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d | \d\d\d.\d\d\d.\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242, your phone is 254.165.4527')
print('Phone number found: ' + mo.group())

mo = phoneNumRegex.findall('My number is 415-555-4242, your phone is 254.165.4527')
print(mo)
#print('Phone number found: '+ mo.group())

emailRegex = re.compile(r'[a-zA-Z0-9._%+-]+@+[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4})')
em1 = emailRegex.search("this is my email address ckronber@gmail.com")
print("email: " + em1.group())