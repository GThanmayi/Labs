import re
txt="ERROR error Error"
print(re.findall(r"error",txt))
# here it prints only the lower case letters
print(re.findall(r"error",txt,re.I))