num = 91494
num1 = str(num)
size = len(num1)
fullNum = ""

for i in range(size):
    strNum = num1[size-1-i]
    strNum = int(strNum)
    strNum **= 2
    strNum = str(strNum)
    fullNum += strNum
    
intNum = int(fullNum)
    
print(intNum)