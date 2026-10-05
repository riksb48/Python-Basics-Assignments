import re

s = input("Enter string: ")
if s.isalnum():
    print("Valid - Only a-z, A-Z, 0-9")
else:
    print("Invalid - Contains special character")

pattern = r'^[a-zA-Z0-9]+$'
if re.match(pattern, s):
    print("Valid String")
else:
    print("Invalid String")
