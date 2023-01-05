'''
Private access specifier
========================



'''

class student:
    
    def getdata(self):

        self.__name=input("Enter Name: ")
        self.__rno=input("Enter Roll Number: ")
        self.__display()
        
    def __display(self):

        print("Student Name: ",self.__name)
        print("Roll Number: ",self.__rno)

s1=student()
s1.getdata()

#print("Name: "s1.__name) #Error: AttributeError: 'student' object has no attribute '__name'
#print("Roll Number"s1.__rno)
#s1.__display()#Error: AttributeError: 'student' object has no attribute '__display'
