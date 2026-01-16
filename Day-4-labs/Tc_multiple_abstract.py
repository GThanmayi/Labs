from abc import ABC, abstractmethod
class Bank(ABC):
    @abstractmethod
    def interest(self):
        pass
    @abstractmethod
    def loan(self):
        pass

class SBI(Bank):
    def interest(self):
        print("interst is 6%")
    def loan(self):
        print("loan is available")

s=SBI()
s.interest()
s.loan()
