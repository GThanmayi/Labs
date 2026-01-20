import re

txt = "Hello\nhello"
pattern = r"hello."
print(re.findall(pattern, txt, flags=re.IGNORECASE | re.MULTILINE))
print(re.findall(r".+", txt, flags=re.DOTALL))