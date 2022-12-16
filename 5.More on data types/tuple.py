'''
tuple
======
1) It is collection of dissimilar datatype elements.
2) Elements in the tuple are enclosed in round brackets [parenthesis]
3)They are immutable. 

'''
t=(10,20,'itvedant',89.0,'E-class',20)
print(t)
print(type(t))

#len

n=len(t)
print("total number of elements in tuple: ",n)

#accessing tuple element with index
'''
                        t
          (10,20,'Itvedant',89.9,'Eclass')
           0  1      2       3       4
           -5-4     -3      -2      -1

     syntax:

            tuple_variable[index_pos]

            
'''
'''


n=len(t)
print(n)


s=t[::-1]
print("reverse",s)



'''
'''
Two methods or function supported in tuple.
1)count():It is  used to count occurance of the element in the
          tuple.
2)index():This method or function returns index of the
          elements given.

'''

#count the reapeated tuple
n=t.count(20)
print("total number of occurance: ",n)


#print the index number by tuple elemet
ipos=t.index('itvedant')
print("Index position is: ",ipos)

ipos=t.index(20)
print("Index position is: ",ipos)

'''
for i in range(0,len(t)):

    if t[i]==20:

        print(i)

'''

del t
print(t)
