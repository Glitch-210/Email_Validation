import re

condition = r"^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
# r = raw strings
# adding the r before the string, Python treats 
# backslashes' as literal characters,
# preserving your intended regex pattern.
print("Email must contain numerical values and alphabets")
user = input("Enter your email: ")
if  re.search(condition,user):
    print("Correct Email! ")
else:   
    print("Wrong Email!!!!")