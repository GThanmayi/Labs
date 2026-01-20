class calc:
    def add(self,a,b):
        return a+b

class Advancedcalc(calc):
    def add(self,a,b):
        return a+b

    def sub(self,a,b):
        return a-b

c=Advancedcalc()
print(c.add(10,20))
print(c.sub(10,20))
print(c.add(10,30))