class Oper:
    def __init__(self,value):
        self.value=value

    def __add__(self,other):
        return self.value+self.value+other.value

b1=Oper(10)
b2=Oper(20)

print(b1+b2)