#abundant number:the sum of the factors is greater than the number
#number from user
n=int(input())
#intialising sum as 1 because 1 is divisor of every number
sum=1
for i in range(2,n):
    if n%2==0:
        sum=sum+i
if sum>n:
    print("Abundant number")
else:
    print("not an abundant number")
#alternate method
i=2
import math
while i<=math.sqrt(n):
    if n%2==0:
        if n//i==i:
            sum=sum+i
        else:
            sum=sum+i+n/i
            i=i+1
if sum>n:
    print(n," is an abundant number")
else:
    print(n," is not an abundant number")
