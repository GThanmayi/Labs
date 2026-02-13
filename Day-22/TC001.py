import mysql.connector

host = "localhost"
user = "root"
password = "123456789"
database = "feb2026"
conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
cursor = conn.cursor()
print("connected to the database successfully")
Query1 = "SELECT * FROM employee"
cursor.execute(Query1)
result = cursor.fetchall()
for row in result:
    print(row)

