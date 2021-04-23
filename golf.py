data = [[18,20],[45,2],[61,12],[37,6],[21,21],[78,9]]
output = []
size = len(data)

for i in range(size):
    if((data[i][0] >= 55) & (data[i][1] > 7)):
        output.append("Senior")
    else:
        output.append("Open")
        
print (output)