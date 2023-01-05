n1=int(input("Enter first value: "))
n2=int(input("Enter second value: "))

def arithmatic(x,y):
    add=x+y
    sub=x-y
    mul=x*y
    div=x/y

    return add,sub,mul,div

a,b,c,d=arithmatic(n1,n2)

print("Addition is: ",a)
print("Substraction is: ",b)
print("Multiplication is: ",c)
print("dicision is: ",d)
