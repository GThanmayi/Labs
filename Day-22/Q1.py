import mysql.connector

# 1. Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",       # your host
    user="root",   # your MySQL username
    password="123456789", # your MySQL password
    database="feb2026"   # database name
)

cursor = conn.cursor()

# 2. Fetch all employees with salary > 50000
print("Employee with salary > 50000:")
query_fetch = "SELECT id, name, salary FROM employee WHERE salary > 50000"
cursor.execute(query_fetch)
results = cursor.fetchall()
for row in results:
    print(row)

# 3. Insert a new employee
print("\nInserting a new employee...")
query_insert = """
INSERT INTO employee (id, name, salary)
VALUES (%s, %s, %s)
"""
new_employee = (101, "John Doe", 55000)
cursor.execute(query_insert, new_employee)
conn.commit()
print("Inserted:", new_employee)

# 4. Update salary of a specific employee by 10%
print("\nUpdating salary by 10% for employee with id 101...")
query_update = "UPDATE employee SET salary = salary * 1.10 WHERE id = %s"
cursor.execute(query_update, (101,))
conn.commit()
print("Salary updated for employee id 101")

# 5. Close the connection
cursor.close()
conn.close()
