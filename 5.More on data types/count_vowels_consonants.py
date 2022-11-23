'''
Find number of vowels and consonants in the string entered
by user.

a,e,i,o,u,A,E,I,O,U
'''

str=input("enter string:")
print(str)
v=0
c=0
for x in str:
    print(x)
    if x in ('a','e','i','o','u','A','E','I','O','U'):
        v+=1 #v=v+1
    else:
        c+=1 #c=c+1
print("total number of vowels: ",v)
print("total number of consonents: ",c)
