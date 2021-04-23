def main():
    a = 3
    b = 4
    print("Hello World")

#This is how you declare the main function in python    
if __name__ == "__main__":
    main()
    
    #declare f as a variable
    f = 0
    print (f)
    
    #declare f as a string
    f = "abc"
    print(f)
    
    #string varable and integers
    print("this is a string " + str(123))
    
    #Global vs local variables in functions
    def someFunction():
        global f 
        f = "def"
        print(f)
        
    someFunction()
    print(f)
    