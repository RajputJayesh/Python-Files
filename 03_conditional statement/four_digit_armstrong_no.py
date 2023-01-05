'''
A four digit number is entered through the keyboard. Write a program to check
whether number is a Armstrong number.

n=8208

'''

n=int(input("Enter three digit number")) #8208

a=n%10      #8208%10 = 8
b=n//10     #8208//10 = 820
c=b%10      #820%10 = 0
d=b//10     #820//10 =82
e=d%10      #82%10= 2
f=d//10     #82//10= 8
s=a**4+e**4+c**4+f**4

if s==n:
    print("it is Armstrong number")
else:
    print("it is not Armstrong number")









