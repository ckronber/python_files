#number of resistors in the array
numRes = 56
#2d map for adding all values of resistors
hexMap = [0]*numRes

resVals = []
resVals.append(.34)
resVals.append(.64)
resVals.append(1)
resVals.append(1.81)
resVals.append(2)
resVals.append(3.33)
resVals.append(4)
resVals.append(5)
resVals.append(6)
resVals.append(7)
resVals.append(8)
resVals.append(10)
resVals.append(20)
resVals.append(30)
resVals.append(40)
resVals.append(47)
resVals.append(50)
resVals.append(60)
resVals.append(70)
resVals.append(80)
resVals.append(90)
resVals.append(94)
resVals.append(100)
resVals.append(120)
resVals.append(141)
resVals.append(188)
resVals.append(235)
resVals.append(282)
resVals.append(300)
resVals.append(400)
resVals.append(500)
resVals.append(600)
resVals.append(700)
resVals.append(800)
resVals.append(900)
resVals.append(1000)
resVals.append(2000)
resVals.append(3000)
resVals.append(4000)
resVals.append(5000)
resVals.append(6000)
resVals.append(7000)
resVals.append(8000)
resVals.append(9000)
resVals.append(10000)
resVals.append(20000)
resVals.append(30000)
resVals.append(40000)
resVals.append(50000)
resVals.append(60000)
resVals.append(70000)
resVals.append(80000)
resVals.append(90000)
resVals.append(100000)
resVals.append(500000)
resVals.append(1000000)


#.34 ohms resistance
hexMap[0] = 0xDB6DB6C36DB600000000
#.64 ohms resistance
hexMap[1] = 0xDB6DB0C36DB600000000
#1 ohms resistance
hexMap[2] = 0x00003000000000000000
#1.81 ohms resistance
hexMap[3] = 0xDB6D80C366DB60000000
#2 ohms resistance
hexMap[4] = 0x0000000001B600000000
#3.33 ohms resistance
hexMap[5] = 0x000006DB6C0600000000
#4 ohms resistance
hexMap[6] = 0x000006DB600600000000
#5 ohms resistance
hexMap[7] = 0x000006DB000600000000
#6 ohms resistance
hexMap[8] = 0x0000B01B6A8600000000  
#7 ohms resistance 
hexMap[9] = 0x0000B01B6A5600000000

#Currently Working on this value
#8 ohms resistance
hexMap[10] = 0xDB6DB6DB6D8600000000
#10 ohms resistance
hexMap[11] = 0xDB6DB6DB6D8600000000
#20 ohms resistance
hexMap[12] = 0xDB6DB6DB6D8600000000
#30 ohms resistance
hexMap[13] = 0xDB6DB6DB6D8600000000
#40 ohms resistance
hexMap[14] = 0xDB6DB6DB6D8600000000
#47 ohms resistance
hexMap[15] = 0xDB6DB6DB6D8600000000
#50 ohms resistance
hexMap[16] = 0xDB6DB6DB6D8600000000
#60 ohms resistance
hexMap[17] = 0xDB6DB6DB6D8600000000
#70 ohms resistance
hexMap[18] = 0xDB6DB6DB6D8600000000
#80 ohms resistance
hexMap[19] = 0xDB6DB6DB6D8600000000
#90 ohms resistance
hexMap[20] = 0xDB6DB6DB6D8600000000
#94 ohms resistance
hexMap[21] = 0xDB6DB6DB6D8600000000
#100 ohms resistance
hexMap[22] = 0xDB6DB6DB6D8600000000
#120 ohms resistance
hexMap[23] = 0xDB6DB6DB6D8600000000
#141 ohms resistance
hexMap[24] = 0xDB6DB6DB6D8600000000
#188 ohms resistance
hexMap[25] = 0xDB6DB6DB6D8600000000
#235 ohms resistance
hexMap[26] = 0xDB6DB6DB6D8600000000
#282 ohms resistance
hexMap[27] = 0xDB6DB6DB6D8600000000

print(hexMap)

hexMask1 = 0xFF
hexVal = hexMap[0]
hexVals = []

# number of chips
chipNum = int((len(str(hexVal))-3)/2)

#adding 0s to the hexmask
hexMask1 = hexMask1 << ((chipNum-1)*2)*4
hexMasks = [hexMask1]

#This adds all the masks used in a list
for i in range(chipNum-1):
    hexMasks.append(hexMasks[0] >> (8*(i+1)))

#hex values are used here and 8 bits are shifted into the shift register at a time  
hexVals = []
for i in range (chipNum):
    hexVals.append((hexMasks[i] & hexVal) >> (8*((chipNum-1)-i)))
    #add the shiftout here to send the data to the shift register only if all the data is sent
print(hexVals)
# This section is if I want to flip shifting from one way to another
#numChips = chipNum + 1    
    
#for i in range(numChips):
#   print(hex(hexVals[(numChips-2)-i]))