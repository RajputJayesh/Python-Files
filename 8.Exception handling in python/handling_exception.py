'''
Handling any exception with Exception parent class.

'''
try:
    x=int(input("enter numerator: "))
    y=int(input("enter denominator: "))
    d=x/y
    print("division is: ",d)
except Exception as e:
    #print("Something went wrong !!!",e)
    print("Error: ",e)
