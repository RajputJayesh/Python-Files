'''
Validation:
===========
Input given by the user is as per rule defined by dveloper
in the application or validating the input.

validate mobile number
======================

1. Check whether it is digit or not=>isdigit()
2. Check wether it is 10 digit.

'''
mob=input("Enter Mobile Number: ")

if mob.isdigit():
    if len(mob)==10:
        print("Valid mobile number")
    else:
        print("invalid mobile number")

else:
    print("Invalid mobile number")
'''
if mob.isdigit() and len(mob)==10:
    print("valid mobile number")
else:
    print("invalid mobile number")
'''
