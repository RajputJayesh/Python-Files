'''
Define class
===========
syntax:

class classname:

     members of class


Members consist of:
1)variables to store data called as data members.
2)Function to perform task called as Member function or Method.
Create object or define object
=============================
syntax

variable=classname()

e.g

class student:

     Members of class



s1=student()

s1 is the object of class student.
Object is also called as instance of the class.
The process of creating object of class is called as
instantiation.

In order to access data members and member function or
methods inside class there is need to create object.

Accessing Member function or method inside class.
objectname.functionname()
objectname.datamembername

'''

class student:

    def greet(self):
        print(self)
        print("Good Evening All")

#greet() NameError: name 'greet' is not defined

s1=student()
    
s1.greet()
print(s1)
'''
The object which is used to call method is passed
as an argument to that method body.
'''
print("Data type of an object: ")
print(type(s1))

x= 10
print("Data type of variable: ")
print(type(x))
