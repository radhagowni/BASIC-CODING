# To calculate the number of times the substring has occured in the given string
string=input("enter string:")
substring=input()
count=0
for i in range(0,len(string)):
    if string.startswith(substring,i):
        count= count+1
print("count :",count)
