string=input()
substring=input()
count=0
for i in range(0,len(string)):
    if string.startswith(substring,i):
        count=count+1
print(count)