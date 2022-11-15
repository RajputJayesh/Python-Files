'''
for loop
========

syntax:
     for variable in range(start,stop,step):

              body of loop to be repeated


variable is a counter variable.

'''

'''
i=11
r=i in range(1,10,1)
print(r)
'''
n=int(input("Enter last term: "))

for i in range(1,n+1,1):
    print(i)

'''
i   i in [1,2,...,9]    print(i)    step 1
1   1 in [1,2,...,9]T    1           2
2   2 in            T    2           3
3   3 in []         T    3           4
.
.
.
.
9   9 in []         T    9           10
10 10 in []         F
'''
