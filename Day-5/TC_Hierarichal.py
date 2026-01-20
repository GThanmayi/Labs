class Parent:
    def parentt1(self):
        print("Parent 1")

class Child1(Parent):
    def c1(self):
        print("child1")
class Child2(Parent):
    def c2(self):
        print("child2")

c1=Child1()
c1.c1()
c1.parentt1()

c2=Child2()
c2.c2()
c2.parentt1()
