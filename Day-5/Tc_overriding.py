class Animal:
    def sound(self):
        print("Animal sound")

class dog(Animal):
    def sound(self):
        print("Dog Barks")

class cat(Animal):
    def sound(self):
        print("Cat Barks")
obj=[dog(),cat()]
for a in obj:
    a.sound()