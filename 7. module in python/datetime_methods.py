'''
                    datetime
        -------------------------------
        |         |                    |
        date     time             datetime   1 level
                                        |
                                        -year()
                                        |
                                        -month() 2nd level
                                        |
                                        -day()
'''

#create datetime

'''
datetime(year,month,day,hour,minute,second)

'''


import datetime 
'''
dt1=datetime.datetime(2022,11,21)
print(dt1)
dt2=datetime.datetime(2022,11,21,20,25,45)
print(dt2)

'''

#to extract sytem date and time use now() method

sysdt=datetime.datetime.now()
print(sysdt)#2022-12-12 13:49:15.510259

y=sysdt.year
print(y)
m=sysdt.month
print(m)
d=sysdt.day
print(d)
hr=sysdt.hour
print(hr)
minu=sysdt.minute
print(minu)
sec=sysdt.second
print(sec)

