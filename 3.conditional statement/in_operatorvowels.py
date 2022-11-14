'''
Write a program to check whether character entered by
user is vowel or consonant.

vowels=> a,e,i,o,u,A,E,I,O,U
consonants: Other than vowels are consonants.

in and not in are called as membership operators.
'''

ch=input("Enter Character: ")
if ch in('a','e','i','o','u','A','E','I','O','U'):
    print("it is vowel")
else:
    print("it is consonant")
