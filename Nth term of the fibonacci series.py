#to print the nth term in fibonacci series
def fib(n):
    if n<2:
        return n
    return fib(n-1)+fib(n-2)
n=int(input("Enter number:"))
print('Nth term is ',fib(n-1))
