#Single level inheritance

class Cse:
    def Hod(self):
        print("Hod name is meena")

class Specialization(Cse):
    def Cyberhod(self):
        print("Cyberhod name is reena")

C=Specialization()
C.Hod()
C.Cyberhod()


#Multilevel inheritance
class Engineering:
    def branches(self):
        print("There are so many branches in engineering")

class Cse(Engineering):
    def Cse(self):
        print("Cse is a branch of engineering")

class Ece(Cse):
    def Ece(self):
        print("Ece is a branch of engineering")

E1=Ece()
E1.Ece()
E1.Cse()
E1.branches()


