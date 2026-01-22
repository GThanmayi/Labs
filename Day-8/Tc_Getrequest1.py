import requests
url ="https://api.restful-api.dev/objects?id=3&id=5&id=10"
response=requests.get(url)
print(response.status_code)
print(response.json())