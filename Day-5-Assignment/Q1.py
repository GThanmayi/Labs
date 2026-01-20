class Vehicle:
    count=0
    def __init__(self):
        Vehicle.count+=1

    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def start1(self):
        print("vehicle1 started")


C=Car()
C.start1()
C.start()
print("No of vehicles created",Vehicle.count)
