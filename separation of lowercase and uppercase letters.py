#taking input from string
string=input()
#initialising empty variables to store upper and lower case letters separately
s=""
r=""
#traversing through string
for i in range(len(string)):
    if string[i].islower():
        s=s+string[i]
    else:
        r=r+string[i]
print("lower case letters: ",s)
print("uppercase letters: ",r)
#alternative way
l=""
m=""
for i in range(len(string)):
    if string[i]>='a'  and string[i]<='z':
        l=l+string[i]
    else:
        m=m+string[i]
print(s)
print(r)
