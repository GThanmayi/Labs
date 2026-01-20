class box1:
    def __init__(self,value):
        self.value=value
    def __add__(self,other):
        return self.value+other.value

b1=box1(3)
b2=box1(48)
print(b1+b2)