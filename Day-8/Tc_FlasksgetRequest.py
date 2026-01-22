import requests
geturl="http://127.0.0.1:5000/users"
response=requests.get(geturl)
print("get status code",response.status_code)
print(response.json())

posturl="http://127.0.0.1:5000/users"
response=requests.post(posturl)
print("post status code",response.status_code)
body1={
    "name":"preethi"
}
r1=requests.post(posturl,json=body1);
print("post status code",r1.status_code)
print(r1.json())

puturl="http://127.0.0.1:5000/users/2"
response=requests.put(puturl)
print("put status code",response.status_code)
body2={
    "name":"Kalki"
}
r2=requests.put(puturl,json=body2);
print("put status code",r2.status_code)
print(r2.json())

patchurl=