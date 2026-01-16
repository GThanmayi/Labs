class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no


    def display(self):
        print("name:",self.name)
        print("roll_no:",self.roll_no)

s1=Student("james",2)
s2=Student("jack",3)
s1.display()
s2.display()
