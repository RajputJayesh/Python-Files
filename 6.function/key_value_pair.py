'''
1. required argument
2. Default argument
3. Key value pair argument.
   key=value


   area of rectangle=length x breadth

           3
    ---------------
   |               |
   |               | 2    area=3x2=6
   |               |
    ---------------
'''



def area(l,b):
    print("Lenght of the reactangle to be manufactured: ",l)
    print("Breadth of the reatangle to be manufactured: ",b)

    area=l*b

    print("Area of reactangle is: ",area)

#area(10,20)#correct parameters

#area(20,10)

#area(l=10,b=20)
    
area(b=10,l=20)
