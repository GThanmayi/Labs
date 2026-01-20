class Animal:
    def spark(self):
        print("Animal makes a sound")

class dog(Animal):
    def bark(self):
        print("dog barks")

d=dog()
d.spark()
d.bark()