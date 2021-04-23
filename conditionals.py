#
# Example file for working with conditional statements
#

def main():
    x,y = 1000, 100
 
 #conditional flow uses if, elif, else
    if(x<y):
        st = "x is less than y"
    elif(x == y):
        st = "x is the same as y"
    else:
        st = "x is greater than y"
        

    print(3 ** 2 + 1 != 30 / 3)
    print((9 - 4) * 2 == 77 / 7 - 1)
 #conditional statement let you use "a if C else b"
    

#This is how you declare the main function in python    
if __name__ == "__main__":
    main()
    
    