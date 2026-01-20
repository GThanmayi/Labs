import re
txt="price of apples is234 in bazar"
result=re.findall(r"is(?=\d+)",txt)
print(result)