#metacharaccters and special sequences
import re
text = "ID: A1 B2 C3 100  abc123   5x7"
print("Any single char:", re.findall(r".", "abc"))
print("Digits:", re.findall(r"\d", text))
print("Words:", re.findall(r"\w+", text))
print("Spaces:", re.findall(r"\s+", text))
print("Pattern with *:", re.findall(r"ab*c", "ac abc abbc"))
print("Pattern with +:", re.findall(r"\d+", text))
print("Optional char with ?:", re.findall(r"5x?7", text))