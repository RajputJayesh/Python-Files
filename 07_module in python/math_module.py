'''
build in modules
=================

               modules
        ---------------------------
        |          |              |
        function   constants     classes


in order to use math module un the python file. then
there is s need ti import that mpdile

step1:import module
step2:use that module

'''
#import math

#factorial
'''

r=math.factorial(4)
print("Factorial of number is: ",r)

'''

#Alisaing module=> giving different name


#import math as m

#ceil() and floor()
'''
ceil()
15.7 => 15 to 16 =>16
15.3 => 15 to 16 =>16
'''
'''
print(m.ceil(15.8))
print(m.ceil(15.5))
print(m.ceil(15.3))

'''

'''
floor()
15.7 => 15 to 16 =>15
15.3 => 15 to 16 =>15
'''

'''
print(m.floor(15.5))
print(m.floor(15.5))
print(m.floor(15.3))
'''


#import specific functionality from module
'''

from math import factorial,sqrt

r=factorial(6)
print("Factorial is: ",r)

sroot=sqrt(25)
print("square root is: ",sroot)

'''

#importing everything from module
'''

from math import*

print(ceil(15.3))
print(floor(15.7))
print(factorial(4))
print(sqrt(16))

'''

'''

import math as m

print("value of PI is: ",m.pi)
print("Value of tau is: ",m.tau)

'''

