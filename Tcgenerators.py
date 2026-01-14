def numbers():
    yield 1
    yield 2
    yield 3
gen=numbers()

print(next(gen))
print(next(gen))
print(next(gen))

def count(n):
    for i in range(1,n+1):
        yield i
for val in count(4):
    print(val)

