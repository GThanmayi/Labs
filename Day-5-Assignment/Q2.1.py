class Calc:
    def add(self,a,b=0,c=0):
        return a+b+c


class newcalc(Calc):
    def add(self,a,b=0,c=0):
        return a+b+c
    def sub(self,a,b=0,c=0):
        return a-b-c

c=newcalc()
print(c.add(10,20))
print(c.sub(10,20))
print(c.add(10,20,30))
print(c.sub(10,20,80))