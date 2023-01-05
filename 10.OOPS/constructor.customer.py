class customer:
    def __init__(self):

        self.bname="SBI"
        self.ifsc="SBIN123456789"
        self.loc="Eclass"
    def getdata(self):

        self.name=input("Enter customer name:")
        self.mob=input("Enter mobile number:")
        self.bal=float(input("Enter account opening balance:"))

    def display(self):

        print("Bank Details:")
        print("-----------------------------------")
        print("Bank Name: ",self.bname)
        print("bank IFSC: ",self.ifsc)
        print("bank location:",self.loc)
        print()
        print("Customer Details")
        print("-----------------------------------")
        print("Customer Name: ",self.name)
        print("Customer Mobile: ",self.mob)
        print("Customer Balance: ",self.bal)

c1=customer() #object created => constructor called
c1.getdata()
c1.display()
print()
c2=customer()
c2.getdata()
c2.display()
