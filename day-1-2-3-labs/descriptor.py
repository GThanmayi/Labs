#adescriptor is an object that defines one or more of the special methods:
def mydescriptor():
    def __get__(self, obj, owner):
        print("getting value")
        return obj._x
    def __set__(self, obj, value):
        print("setting value")
        obj._x = value

class Test:
    x=mydescriptor
t=Test()
t.x=10
print(t.x)