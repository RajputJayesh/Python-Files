'''
random module
'''
import random as r

#random()
'''
x=r.random() #gives fraction values between 0 to 1
print(x)

t=x*10000
print(t)

otp=round(t)
print("otp to be send: ",otp)

'''

otp=round(10000*r.random())
print("otp to be send: ",otp)
