'''
readline():
This method read files line by return list of lines

'''

fp=open("data.txt","r")
d=fp.readlines()

print("Data in the files: ")
print(d)

print(d[0])
print(d[1])

print("Using for loop: ")
for x in d:
    print(x)
