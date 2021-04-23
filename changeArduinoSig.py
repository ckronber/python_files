#Python file to change the signature of arduino based on atmega IC
writeFile = open("/home/ec2-user/environment/Python 3/avrdude.conf","w")
#Using for the Hex signature for the SMD Part
smdChip1 = open("/home/ec2-user/environment/Python 3/avrdude1.conf","r")
#Using for the Hex signature for the development board for Arduino
smdChip2 = open("/home/ec2-user/environment/Python 3/avrdude2.conf","r")

print("This will change the signature based on arduino I would like to program")
wait = input("if using SMD IC type y, otherwise type n: ")

if wait == 'y':
    writeFile.write(smdChip1.read())    #0x1e 0x95 0x16 For SMD Chip
    print("signature = 0x1e 0x95 0x16")
else:
    writeFile.write(smdChip2.read())    #0x1e 0x95 0x0F for Arduino Development Board
    print("signature = 0x1e 0x95 0x0F")
    
writeFile.close()
smdChip1.close()
smdChip2.close()