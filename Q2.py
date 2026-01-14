class PositiveSalary:
    def __get__(self, obj, owner):
        return obj.__dict__.get('_salary')

    def __set__(self, obj, value):
        # Raise an error if the salary is not positive
        if value < 0:
            raise ValueError("Salary must be a positive number")
        obj.__dict__['_salary'] = value

class Employee:
    salary = PositiveSalary()  # salary is controlled by the descriptor

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary   # This calls PositiveSalary.__set__

        # valid employees
emp1=Employee("John", 100000)
print(emp1.name, emp1.salary)
emp2=Employee("Jane", -30000)