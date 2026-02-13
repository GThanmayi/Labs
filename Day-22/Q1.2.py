from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Select the database and collection
db = client["company_db"]
collection = db["employees"]

# Insert a new employee document
new_employee = {
    "name": "Apsana",
    "department": "IT",
    "salary": 65000
}

insert_result = collection.insert_one(new_employee)
print(f"Inserted new employee with ID: {insert_result.inserted_id}")

# Find all employees in the "IT" department
print("\nEmployees in IT department:")
it_employees = collection.find({ "department": "IT" })
for emp in it_employees:
    print(emp)

#  Update salary of an employee with a given name
employee_name_to_update = "Ravi Kumar"
updated_salary = 70000

update_result = collection.update_one(
    { "name": employee_name_to_update },          # filter
    { "$set": { "salary": updated_salary } }       # update
)

print(f"\nMatched {update_result.matched_count} document(s)")
print(f"Modified {update_result.modified_count} document(s)")
