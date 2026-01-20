#matched groups using capturing parentheses
import re
text ="my number is 455-646-777-834"
pattern=r"(\d{3})-(\d{3})-(\d{3})-(\d{3})"
match=re.search(pattern,text)
if match:
    print("full match:",match.group(0))
    print("1st group:",match.group(1))
    print("2nd group:",match.group(2))
    print("3rd group:",match.group(3))
    print("4th group:",match.group(4))