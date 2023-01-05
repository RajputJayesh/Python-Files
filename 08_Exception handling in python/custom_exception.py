'''
Custom Exception
===============
Creating or definig your own exception other that built in
exception.
If you want your error name to be recognised as python exception
it must be derived from the base class Exception
'''

class ItvedantError(Exception):
    pass

x=int(input("enter numerator: "))
y=int(input("enter denominator: "))
if y==0:
    raise ItvedantError('Denominaor cannot be zero!!!')

else:
    d=x/y
    print("Division is: ",d) 
