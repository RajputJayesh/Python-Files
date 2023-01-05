'''
range():This function generate list of numbers in a sequence.
syntax:

     range(start,stop,step)

     start=> initialization
     stop => conditon
     step => increment/decrement [positive or negative]
     
'''

'''
x=list(range(1,10,1))
print(x)

'''

'''
x=list(range(2,20))#default step s 1
print(x)
'''

'''
#No step aand start
x=list(range(20))#default start is 0
print(x)

'''

'''
#error
x=list(range())
print(x)

'''

'''
#range using user input

x=int(input("enter start number: "))
y=int(input("enter stop number: "))
z=int(input("enter step number: "))

r=list(range(x,y,z))
print(r)

'''

x=list(range(15,5,-2))
print(x)


