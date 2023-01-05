'''
Raising  an exception
=====================
                                                                ------ Python
When ther is fault in runtime--Exception is raised--handled by-|
                                    by system                   ------ try..except

Till now exception is raised internally by system,
if there is need to raise an exception , then
use raise keyword to raise an exception.

exeception is raised with respect to certain condition.

syntax to raise exception
=========================

    raise ExceptionName('Message')

'''


x=int(input("enter numerator: "))
y=int(input("enter denominator: "))
if y==0:
    raise ZeroDivisionError('Denominaor cannot be zero!!!')

else:
    d=x/y
    print("Division is: ",d) 
