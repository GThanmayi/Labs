import requests

url = "https://api.restful-api.dev/objects"
response = requests.get(url)
print(response.status_code)
print(response.json())
