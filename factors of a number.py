def find_divisors(n):
    if n<=0:
        return
    else:
        for i in range(1,n+1):
            if n%i==0:
                print(i,end=' ')
print('Factors of ",n,":", )
find_divisors(100)
