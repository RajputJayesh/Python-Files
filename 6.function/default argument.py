'''
Default argument
================

   Number of argument or        Number of variable used to 
   values or variable passed =  receive.

'''
def addition(x,y=0): #y=0 its taking 0 as default value
    #print(x)
    #print(y)
    z=x+y
    print("Addition is: ",z)
    


#addition(10) Error as y value is not passed.
    
addition(10,20)
addition(10)
