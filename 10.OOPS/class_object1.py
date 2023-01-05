'''
Data member and methods
'''

class student:
    def getdata(self):

        self.name=input("Enter Student Name: ")
        self.rno=input("Rnetr Roll Number: ")
    def display(self):

        print("Student Name: ",self.name)
        print("Student Roll Number: ",self.rno)

s1=student()
s1.getdata()
s1.display()

s2=student()
s2.getdata()
s2.display()
'''
              self=s1
                 |
         -----------------
        |                 |
        name             rno
     itvedant            35        

               self=s2
                 |
         -----------------
        |                 |
        name             rno
      Eclass              56


'''
