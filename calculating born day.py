# It is to know the born day of particular person
month=[0,3,3,6,1,4,6,2,5,0,3,5]
day=["sun","mon","tue","wed","thu","fri","sat"]
y=0
date=int(input("Enter date:"))
month1=int(input("Enter month:"))
year=int(input("Enter year:"))
if (year>1600 and year<=1700):
    y=6
elif (year>1700 and year<=1800):
    y=4
elif (year>1800 and year<=1900):
    y=2
elif (year>1900  and year<=2000):
    y=0
elif (year>2000 and year<=2100):
    y=6
bday=day[(date+y+month[month1-1]+((year%100)//4)+(year%100))%7]
print("Birthday :" ,bday)   
