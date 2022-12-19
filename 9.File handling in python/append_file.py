'''
When there is need to preserve old data or new data must be
added at the end of the old data use append mode.

'''

fp=open('data.txt','a')
mn=input("Enter Mobile Number: ")
data=mn+"\n"
fp.write(data)
fp.close()
