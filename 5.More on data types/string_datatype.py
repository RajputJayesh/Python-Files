'''
String
------
1) String is a collection of charecters.
2) They are enclosed in single quote or double quote or
   triple quoted.

'''

#x='itcedant'

'''
x=this is a string
multiline string
itvedant eclass learning
string
'''
x="itvedant-eclass"
print(x)
print(type(x))
#len(): This is used to calculate number of characters in the string.
n=len(x)
print("Total number of charecters: ",n)


#indexing

'''
Need: To process string charecter by charcter , there is a need to
access charecter in the string. Indexing helps you to access charecter
in the string.

There are two types of indexing
1)Positive Indexing
2)Negative Indexing

Positive index                    x

                   I t v e d a n t - E c  l  a  s  s
                   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
Negative Index                  
          I   t   v  e   d   a  n   t -  E  c   l  a  s  s 
        -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
syntax for accessing:
====================
 string_variable[index_number]


'''

'''
print(x[7])
print(x[12])
print(x[-8])
print(x[-12])
'''

#slicing

'''
Need of slicing:
==============
If there is need to extract partial part of the string from
entire string , then use slicing.
1) to reverse string.

syntax:

string_variable[start:stop:step]
                                   x

                   I t v e d a n t - E c  l  a  s  s
                   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14

Extract vedant word from the give string.

start=>2  stop=>8  step=>1

'''

#x1=x[2:8:1]
#x1=x[10:15:1]
#x1=x[2:12:2]#step 2
#x1=x[2:8:]default step in slicing is 1
#x1=x[:8:]default start in slicing is 0
#x1=x[::]#default stop =starting end
#x1=x[15:0:-1]  reverse string
#print(x)
#print(x1)

'''
slicing with negative index

                        Negative Index                  
          I   t   v  e   d   a  n   t -  E  c   l  a  s  s 
          0   1   2  3   4   5  6   7 8  9 10  11 12 13 14
        -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

step=> negative

conclusion:
if step is positive then start=left  end=right
if step is negative then start=right end=left

'''
#x1=x[14:8:-1]
#x1=x[:8:-1] taking start default another side
x1=x[::-1] #reverse string
print(x1)

