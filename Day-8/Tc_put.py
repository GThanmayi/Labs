import requests

geturl="https://api.restful-api.dev/objects"

response=requests.get(geturl)

print("get status code",response.status_code)
print(response.json())

posturl="https://api.restful-api.dev/objects"

body1={
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
}

r1=requests.post(posturl,json=body1);
print("post status code",r1.status_code)
print(r1.json())

puturl="https://api.restful-api.dev/objects/ff8081819782e69e019be4121eac2edf"

body2={
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 2049.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB",
      "color": "silver"
   }
}
r2=requests.put(puturl,json=body2);
print("put status code",r2.status_code)
print(r2.json())