'''
Set
====
1)Set is collections of dissimilar datatype elements.
2)sets are enclosed within curly braces {}
3)sets are mutable.
4)sets are unordered.
   In other data types index position of the element is fixed.
   but in set position of the element changes.
5)sets allows only unique values[no duplication].


'''

s={10,20,'itvedant',89.9,'Eclass'}
print(s)
print(type(s))

#len
n=len(s)
print("Total number of element in the sets: ",n)

#print(s[1])Error

#indexing or accessing elements is not possible in set
#slicing which require index is not possible in set

#for loop over set

#for loop with index-no

for x in s:  #{10,20,'itvedant',89.9,'Eclass'}
    print(x)


#add element in the set

'''
add(): This function is used to add element in the set.

  set_variable.add(value)

'''

s.add('Itvedant-Eclass')
print(s)
s.add(20)
print(s)


#delete or remove element from set

'''
set_variable.remove(value)
'''

s.remove(89.9)
print(s)

del s
print(s)
