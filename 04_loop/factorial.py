'''
Factorial of number entered by user

'''
n=int(input("Enter Number: "))
i=1
f=1
while(i<=n):
    f=f*i 
    i=i+1
print("Factorial is: ",f)

'''
factorial of number entered by User.
===================================

step1: Example

  5!=5*4*3*2*1    4!=1*2*3*4
  or
  5!=1*2*3*4*5

      1 * 2 * 3 * 4 * 5
      -----
        2   * 3
         -----
           6    * 4
            -------
              24    * 5
               --------
                  120
repeatition => multiply and store
        solution    => loop

step2:
       initialization:i=1
       condition     :i<=5  i.e i<=n
       incre/decr    :i+=1


step3:
           f=1 i
         1 f=f*1=1*1=1
         2 f=f*2=1*2=2
         6 f=f*3=2*3=6  ====> f=f*i
        24 f=f*4=6*4=24
        120f=f*5=24*5=120
'''
'''
i   i<=4   f=f*i    i=i+1
1   1<=4T  f=1*1=1  i=1+1=2
2   2<=4T  f=1*2=2  i=2+1=3
3   3<=4T  f=2*3=6  i=3+1=4
4   4<=4T  f=6*4=24 i=4+1=5
5   5<=4F





'''
