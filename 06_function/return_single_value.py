m1=int(input("Enter marks of first subject: "))
m2=int(input("Enter marks of second subject: "))
m3=int(input("Enter marks of third subject: "))

def marksadd(a,b,c):
    t=a+b+c

    return t

tot=marksadd(m1,m2,m3)

print("Total: ",tot)
