import re
text="python is powerful"
result=re.match("python",text)  #it will find the beginning of the string
if result:
    print("match found")
else:
    print("match not found")


searchresult=re.search("python",text)  #it will find the entire text and it will return the python object
print(searchresult.group()) #it will print the python as a text
print(searchresult.start())#it will print the starting index
print(searchresult.end())

email="admin@gmail.com"
if re.match(r"[a-zA-Z]+@",email):
    print("valid start")


result2=re.fullmatch(r"\d{10}","123456789")
print(result2)

print(re.findall(r"\d+","price 50 and 100 and 200"))
for n in re.finditer(r"\d+","A1, B33, C444"):
    print(n.group(),n.start(),n.end())

for n in re.finditer(r"[a-z]", "a1 b1000, B33, C444"):
    print(n.group(), n.start(), n.end())
for n in re.finditer(r"[A-Z]", "a1 b1000, B33, C444"):
    print(n.group(), n.start(), n.end())

print(re.search(r"\d+","Age is 25"))
print(re.search(r"^a.*c$","anhgyuibh"))
m=re.search(r"\w+(?=@)","test@gmail.com")
print(m.group())



print(re.search("python","Python",re.I))
text4="one\ntwo\nthree"
re.findall(r"^t\w+",text4,re.M)
