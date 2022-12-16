'''
s='Itvedant-Eclass'
print(s)
print(type(s))

sup=s.upper()
print(sup) #ITVEDANT-ECLASS

slow=sup.lower()
print(slow) #itvedant-eclass
'''

#isalpha()
'''
This method check whether entire string contains alphabhets.
if all string element are alphabhets then it return true or it
returns false.

'''
'''

#s="itvedant-eclass"  output:-false
#s="itvedant eclass"  output:-false
s="itvedanteclass" #output:- true

r=s.isalpha()
print(r)

'''

#isdegit():
'''
This method is used to check whether string
elements are digit i.e 0,1,2,3..9
It returns true if string contains all digits.
It return false if string contains other than digits.
'''

'''
s="1234567"
r=s.isdigit()
print(r)
'''

#split()
'''
When there is need to convert a string into list,spilt()
method is used.

syntax:
=======

    str_variable.split('seprator')

'''

'''
#s='We are learning,string methods,in todays class'
s='We are learning-string methods-in todays -class'
print(s)
#l=s.split(',')
l=s.split('-')
print(l)
print(type(l))
'''

s='We are learning string methods in todays class'
l=s.split()
print(l)
#default seprator is space.

'''
Join     => iterable into string.
replace()=> 

'''
