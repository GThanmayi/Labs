from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["feb2k26k"]
collection = db["employees"]

new_employee = {
    "name": "ThanmayiThanu",
    "department": "CSE",
    "salary": 85000
}

# Insert the document
insert_result = collection.insert_one(new_employee)
print(f"\nInserted new employee with ID: {insert_result.inserted_id}")

# Find the document using its _id
employee = collection.find_one({ "_id": insert_result.inserted_id })
print("\nDetails of inserted employee:", employee)
