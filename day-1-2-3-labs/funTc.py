def add(a,b):
    print(a+b)
add(10,20)

def sub(a,b):
    return a-b

print(sub(100,20))

def hello(greeting="hello",name="world"):
    print('%s,%s'%(greeting,name))

hello()
hello('greetings','deepa')

def print_param(*params):
    print(params)

print_param('testing')
print_param(1,2,3,4)

def print_param1(**params):
    print(params)

print_param1(x=1,y=2,z=3)
