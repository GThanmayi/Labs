class student:
    name="ravi"
    age=25

s1=student()
print(s1.name)
print(s1.age)

class employees:
    def __init__(self,name,age):
        self.name=name
        self.age=age

e1=employees("leena",30)
print(e1.name,e1.age)