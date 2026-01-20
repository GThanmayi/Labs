import re
email=input("Enter your email: ")
result=re.search(r"[a-zA-z0-9]+@gmail.com",email)
if result:
    print("valid start of email")
else:
    print("invalid start of email")