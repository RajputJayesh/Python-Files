'''
Any digit number is entered by user.
1) WAP to reverse that number.
2) Find sum of digits.

1st Iteration          2nd                  3rd

   n=6778               n=677               n=67

   r=n%10=6778%10=8     r=n%10=677%10=7     r=n%10=67%10=7
   print(8)             print(7)            print(7)
   n=n//10=6778//10=677 n=n//10=677//10=67  n=n//10=6
4th                  n=0 stop
   n=6
   r=n%10=6%10=6
   print(6)
   n=n//10=6//10=0

                0  => Quotient
             --------
          10|   6
             -  0
             -------
                6 => Remainder

n=874
'''
'''
n=874


1st

r=n%10  =  874%10 = 4
print(4)
n=n//10 =  874//10 = 87

2nd
n=87

r=n%10 =  87%10 = 7
print(7)
n=n//10 = 87//10= 8

3rd
n=8

r=n%10= 8%10 = 8
print(8)
n=n//10 = 8//10 =0


'''


n=int(input("Enter Number: "))

while n!=0:

    r=n%10
    print(r)
    n=n//10

    
