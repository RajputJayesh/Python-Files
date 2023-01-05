'''
Multiple inheritance
====================
The inheritance in which there are many base classes but only
one derived class is called as Multiple inheritance.

                B1  B2   B3 ........Bn
                 |   |    |         |
                  ------------------
                          |
                          D
syntax:
class D(B1,B2,B3,....,Bn):

     body of derived clas

                  A        B
                  |        |
                   --------
                      |
                      C
'''

class A:

    def geta(self):
        self.a=int(input("Enter value of a: "))

class B:

    def getb(self):
        self.b=int(input("Enter value of b: "))

class C(A,B):

    def addition(self):
        res=self.a+self.b
        print("Addition is: ",res)

c1=C() #derived class object created
c1.geta()
c1.getb()
c1.addition()
