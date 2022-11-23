'''
List
====

1) List is collection of dissimilar datatypes elements.
2) Element in list are enclosed in square brackets.
3) List is mutable.[once defined they can be changed.]

'''

#Define list

l=[10,89.7,-3,45.6,'ivedant']
print(l)
print(type(l))

#len()

n=len(l)
print("total number of elements in the list: ",n)

#indexing
'''
                       l
                       
          [10,89.7,-3,45.6,'Itvedant']
           0   1    2  3       4
           -5  -4  -3  -2      -1
           
Accessing list element
    syntax:

        list_variable[index_value]
'''
print(l[3])
print(l[-4])

#slicing
l1=l[1:4:1]
print(l1)
lrev=l[::-1]
print(lrev)

#for loop over list

print("with index: ")

for i in range(0,len(l),1):
    print(l[i])


print("without index: ")

for i in l: #[10, 89.7, -3, 45.6, 'ivedant']
    print(i)



