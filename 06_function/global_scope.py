'''
Scope of variable 
=================

the region in the program where value can be accssed is
called as scope of variable.

or
life of a variable.

there are two types of scope:

1)Local scope
2)Global scope

'''

x=10

print("value of variable x outside function: ",x)

def scope_variable():
    print("value of variable inside function: ",x)

scope_variable()


'''
The variable that is defined outside the function and whose value
can be accessed outside as well as inside the function is called
as Global Variable. 

'''

