'''
Hirarchical Inheritance
======================
The inheritance in which there is one base class and many derived
classes is called as Hirarchical Inheritance.

                                B
                                |
                    -------------------------------
                   |      |     |      |           |
                   D1    D2     D3     D4 .........Dn


e.g                        A
                           |
                     --------------
                    |              |
                    B              C

'''

class A:

    def geta(self):
        self.a=int(input("Enter value of a: "))

class B(A):

    def getb(self):
        self.b=int(input("Enter value of b: "))
    def addition(self):
        r1=self.a+self.b
        print("Addition of a and b is: ",r1)

class C(A):

    def getc(self):
        self.b=int(input("Enter value of c: "))
    def addition(self):
        r2=self.a+self.b
        print("Addition of a and b is: ",r2)

b1=B() #derived class object B created.
b1.geta()
b1.getb()
b1.addition()
print()
c1=C() #derived class object C created.
c1.geta()
c1.getc()
c1.addition()


