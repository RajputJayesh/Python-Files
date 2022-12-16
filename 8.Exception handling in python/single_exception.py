'''
Handling exception can be done using following instruction.

try:

    code to be insepected for Exception
    or
    code in which there is chance of
    getting execption.

except ExceptionName:

   except block to given msg.

'''

x=int(input("enter numerator: "))
y=int(input("enter denominator: "))
try:
    d=x/y
    print("division is: ",d)
except ZeroDivisionError:
    print("Denominator cannot be zero,please enter number other than zero")
