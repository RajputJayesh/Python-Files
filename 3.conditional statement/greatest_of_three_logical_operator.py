'''
Gretest of the three number using logical operator.

'''

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if a>b and a>c:
    print(a," is greater")
if b>a and b>c:
    print(b," is greater")
if c>a and c>b:
    print(c," is greater")
