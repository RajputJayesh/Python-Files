'''
A number and its power is entered by the user. Write a program
to find one number raised to another number.

e.g:
n=2
p=3

2^3=8

t=2*2*2

       2 * 2 *  2
       -----
         4   *  2
         --------
            8
2^5
t=2*2*2*2*2

       2 * 2 * 2 * 2 * 2
       -----
         4   * 2
         -------
             8   * 2
             -------
                16   * 2
                --------
                   32

Note: Loop repeatation is govern by power.
loop
initialization:i=1
condition     :
incre/decre   :
2^5
       
         t=1
       2 t=t*2=1*2=2
       4 t=t*2=2*2=4
       8 t=t*2=4*2=8   =====>
       16t=t*2=8*2=16
       32t=t*2=16*2=32

'''
n=int(input("enter number: "))
p=int(input("enter the power of number: "))
i=1
while n<=p:
    i=i+1
    
    print("power is: ",n)
'''
if n<=p:
    i=i+1
    i=i+n
    print("power is: ",i)
'''
