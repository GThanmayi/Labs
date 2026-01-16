def fib(n):
    a,b=0,1
    while n>0:
        c=a+b
        yield a
        a=b
        b=c
        n=n-1

for num in fib(10):
    print(num)