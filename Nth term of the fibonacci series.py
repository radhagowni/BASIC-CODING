def fib(n):
    if n<2:
        return n
    return fib(n-1)+fib(n-2)
n=int(input())
print('Nth term is',fib(n-1))