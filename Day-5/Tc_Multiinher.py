class A:
    def showA(self):
        print("I am A")

class B:
    def showB(self):
        print("I am B")

class C(A,B):
    pass
c=C()
c.showA()
c.showB()