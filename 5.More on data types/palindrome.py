'''
Check whether string entered by user is palindrom
or not

            N I T I N
            -------->
            <--------

    if original string == reversed string  => It is palindrome
algo
===
step1:start
step2:reversed string entered by user.
step3:check reversed and original string
step4:if both are equal then its palindrome otherwise not.

reversed  ===>  [::-1]
'''

org=input("Enter String: ")
rev=org[::-1]
print("Original String: ",org)
print("Reverse String: ",rev)

if org==rev:
    print(rev,"it is palndrome")
else:
    print(org,"it is not a palindrom")
