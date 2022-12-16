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
'''
print(l[3])
print(l[-4])

#slicing
l1=l[1:4:1]
print(l1)
lrev=l[::-1]
print(lrev)
'''
#for loop over list


'''

print("with index: ")

for i in range(0,len(l),1):
    print(l[i])


print("without index: ")

for i in l: #[10, 89.7, -3, 45.6, 'ivedant']
    print(i)

'''

#Add element in the list

'''
There are two methods or function to add element in
the list.
1) Append():
    This function or method is used to add element at the
    end of the list.

    Syntax:
        list_vaeriable.append(element)
        
    
2)insert():
  This function or method is used to add element at
  specific index position

  list_variable.insert(index_pos,value)

'''

l.append(24.5)
print(l)

l.append('Eclass')
print(l)

l.insert(3,50)
print(l)


#update list element

'''
syntax:

  list_variable[index_pos]=value

'''
l[4]="itvedant-Eclass"
print(l)


#delete or remove list elements.

'''
pop(): This is used to delete last elements.

pop(index): This remove specific element whose index is
            mentioned in the pop() method.




'''
l.pop()
print(l)

l.pop(2)
print(l)

#del: keyword used to delete entire list at once.
'''
del l
print(l)
'''

'''
Find summation of the integer elements in the list.

                l
        [10,20,35,1,2,-3]
         0  1  2  3 4  5

         sum=0
sum=sum+10=0+10=10
         sum=sum+20=10+20=30
         sum=sum+35=30+35=65  ===> sum=sum+i
         sum=sum+1=65+1=66
         sum=sum+2=66+2=68
         sum=sum+(-3)=sum-3=68-3=65

         sum=sum+l[0]
         sum=sum+l[1]
         sum=sum+l[2]===> sum=sum+l[i]
         sum=sum+l[3]
         sum=sum+l[4]
         sum=sum+l[5]

'''
l=[10,20,35,1,2,-3]
sum=0
for x in l:  #l=[10,20,35,1,2,-3]
    print(x) 
    sum=sum+x  # 0+10=10,10+20=30, 30+35=65, 65+1=66,66+2=68, 68-3=65
print("Summation is: ",sum)

