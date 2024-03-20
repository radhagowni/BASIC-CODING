n=int(input('enter number:'))
fact=1
if n<2:
    print('not possible')
elif n==0:
    print('1')
for i in range(1,n+1):
    fact=fact*i
print('factorial of a number:',fact)