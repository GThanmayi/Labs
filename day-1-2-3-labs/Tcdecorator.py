#decorator Takes another function and returns a new one
def mydecorator(func):#func refers to the sayhello()
    def wrapper():
        print("Before Function Call")
        func()
        print("After Function Call")
    return wrapper

@mydecorator
def sayhello():
    print("Hello")
    #sayhello = mydecorator(sayhello)
sayhello()#sayhello now refers to the wrapper() function