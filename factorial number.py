n=int(input('Enter number:'))
fact=1
if n==0 or n==1:
    print(1)
for i in range(1,n+1):
    fact=fact*i
print('Factorial of a number:',fact)
