'''
Inheritance
===========

Need
-----
e.g:

class A:

   def getdata(self):

      .......
      .......

   def displayA(self):

      ........
      ........
class B:

   def getdata(self):
      .......
      .......

   def displayB(self):
      ........
      ........
Method getdata() defined in class A, same method is required
in class B, as a result we need to rewrite that method again
in the class B which give rise to code repeatition.

In order to reuse the property of one class into another class
there is need of inheritance.
what is inheritance?
===================
The mechanism or process of deriving one class from another class
to achieve reusability of code is called as Inheritance.

The class from which another class is derived is called as
Base class or parent class.

The class which is derived from another class is called as
derived class or child class.
                            A  parent or base class
                            |
                            |
                            |
                            B child or derived class

Properties of class A or base class [data member and methods]
are now available to derived class or child class.

Syntax for derive class
=======================

class Derivedclassname(baseclassname):

      derived class Body

e.g:

class A:

    body of class A


class B(A):

   body of class B


Type of Inheritance:
===================
1)Single inheritance
2)Multilevel inheritance
3)Multiple inheritance
4)Hierarchical Inheritance
5)Hybrid Inheritance
'''

'''
Single Inheritance:
==================
The inheritance in which there is only one base class and
one derived class is called as Single inheritance.

                         A base class
                         |
                         |
                         |
                         B Derived class
                         
In class A

method     =>geta()
data member=>a

class B
method      => getb()
data member => b
'''

class A:
    def geta(self):
        self.a=int(input("Enter value of a: "))

class B(A):
    def getb(self):
        self.b=int(input("Enter value of b: "))

    def addition(self):

        res=self.a+self.b
        print("Addition is: ",res)

b1=B() # derived class object
b1.geta()
b1.getb()
b1.addition()
