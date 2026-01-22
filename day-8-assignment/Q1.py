import requests
import json

url = "https://jsonplaceholder.typicode.com/users"

headers = {
    "Content-Type": "application/json",
    "User-Agent": "Python-Requests"
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    users = response.json()

    extracted_data = []
    for user in users:
        extracted_data.append({
            "id": user["id"],
            "name": user["name"],
            "email": user["email"]
        })

    with open("users_data.json", "w") as file:
        json.dump(extracted_data, file, indent=4)

    print("Data saved successfully")
    print(extracted_data)

except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)

except requests.exceptions.RequestException as e:
    print("Request Error:", e)