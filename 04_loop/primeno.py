n=int(input("Enter Number: "))

for i in range(2,n,1):
    r=n%i
    if r==0:
        print(n,"It is Non-prime number")
        break
else:
    print(n,"It is Prime Number")
