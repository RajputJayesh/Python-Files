'''
calculator: console based Application
===========

1.Addition
2.Substraction
3.Multiplication
4.Division
5.Exit

Enter your choice:2

'''
while True:
    print("1.Addition")
    print("2.substraction")
    print("3.multiplication")
    print("4.division")
    print("5.exit")
    print()
    ch=int(input("Enter your choice: "))

    if ch==1:
        x=int(input("Enter first number: "))
        y=int(input("Enter second number: "))
        z=x+y
        print("Addition is: ",z)
    elif ch==2:
        x=int(input("Enter first number: "))
        y=int(input("Enter second number: "))
        z=x-y
        print("substraction is: ",z)
    elif ch==3:
        x=int(input("Enter first number: "))
        y=int(input("Enter second number: "))
        z=x*y
        print("multiplication is: ",z)
    elif ch==4:
        x=int(input("Enter first number: "))
        y=int(input("Enter second number: "))
        z=x/y
        print("divition is: ",z)
    elif ch==5:
        print("Exit from program!!")
        break
    else:
        print("Enter valid choice between 1 to 5!!!!")
        
