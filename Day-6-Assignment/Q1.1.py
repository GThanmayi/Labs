import re
EmployeeId=input("Enter employee Id").strip()
result=re.match(r"Emp\d{3}$",EmployeeId)
if result:
    print("Employee Id: found")
else:
    print("Employee Id: not found")